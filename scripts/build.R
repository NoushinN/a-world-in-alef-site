# Run from RStudio: source("scripts/build.R")
if (!requireNamespace("blogdown", quietly = TRUE)) stop("Run scripts/setup.R first.")
blogdown::build_site(build_rmd = TRUE)
