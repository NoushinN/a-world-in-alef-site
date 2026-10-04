# Run once from the project root in the RStudio Console:
# source("scripts/setup.R")
if (!requireNamespace("blogdown", quietly = TRUE)) {
  install.packages("blogdown", repos = "https://cloud.r-project.org")
}
options(blogdown.hugo.version = "0.147.9", blogdown.hugo.extended = FALSE)
blogdown::install_hugo(version = "0.147.9", extended = FALSE)
message("Ready. Run blogdown::serve_site() to preview.")
