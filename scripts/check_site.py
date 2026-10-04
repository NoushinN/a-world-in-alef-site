#!/usr/bin/env python3
"""Check generated internal links and media. No network or extra packages needed."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'public').resolve()
if not (root/'index.html').exists(): raise SystemExit('Build the site with Hugo first.')
class Links(HTMLParser):
 def __init__(self): super().__init__(); self.refs=[]; self.canonical=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href','')
  if tag in ('a','img','script','link'):
   v=a.get('src') if tag in ('img','script') else a.get('href')
   if v:self.refs.append(v)
home=Links();home.feed((root/'index.html').read_text(encoding='utf-8'))
base=urlparse(home.canonical);prefix=base.path.rstrip('/')
errors=[];count=0
for file in root.rglob('*.html'):
 p=Links();p.feed(file.read_text(encoding='utf-8'));count+=1
 for ref in p.refs:
  if ref.startswith(('#','mailto:','data:','tel:')):continue
  u=urlparse(ref)
  if u.netloc and u.netloc!=base.netloc:continue
  path=unquote(u.path)
  if path.startswith('/'):
   if prefix and not (path==prefix or path.startswith(prefix+'/')):
    errors.append(f'{file.relative_to(root)}: link escapes project base: {ref}');continue
   target=root/path[len(prefix):].lstrip('/')
  else:target=file.parent/path
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{file.relative_to(root)}: missing {ref}')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: internal links and assets across {count} generated HTML pages. Base path: {prefix or "/"}')
