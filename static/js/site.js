"use strict";
const filters=document.querySelector('.filters');
if(filters){
  filters.hidden=false;
  const query=document.querySelector('#lesson-search');
  const phase=document.querySelector('#phase-filter');
  const cards=[...document.querySelectorAll('.lesson-card')];
  const update=()=>{
    const needle=query.value.trim().toLocaleLowerCase();let visible=0;
    for(const card of cards){const show=(!needle||card.dataset.search.includes(needle))&&(phase.value==='all'||card.dataset.phase===phase.value);card.hidden=!show;if(show)visible++;}
    for(const section of document.querySelectorAll('.phase'))section.hidden=![...section.querySelectorAll('.lesson-card')].some(card=>!card.hidden);
    document.querySelector('#lesson-count').textContent=`${visible} of ${cards.length} lessons`;
    document.querySelector('#no-results').hidden=visible!==0;
  };
  query.addEventListener('input',update);phase.addEventListener('change',update);update();
}
