# # [Documentation Workflow](http://r-pkgs.had.co.nz/man.html#man-workflow)

# Documentation is a non-trivial effort. However, if there are any plans
# for the author or others to use the code in the future, **do it**.
# Since this project is based upon devtools process, we will continue to 
# use devtools which uses [roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html)

# Using documentation in CDSW is straight forward and consistent with R-Cran & RStudio:
?devtools::document

# The source code that we copied in to our project R folder already has documentation!
# Have a look at the first function in [polyreg_r.R](../files/R/polyreg/R/polyreg_r.R)
con <- file("R/polyreg/R/polyreg_r.R","r")
cat(paste(readLines(con)[1:20],collapse="\n")[1])
close(con)

# The notation **#'** indicates a [roxygen2](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) comment.
# The documentation workflow is:
#  * 1) Add [roxygen](https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html) comment to [R](../files/R/polyreg/R/) files.
#  * 2) Run **devtools::document(<PATH>)**
#  * 3) Explore documentation with *?*
#  * 4) Rinse & Repeat

devtools::load_all("/home/cdsw/R/polyreg")
help(polyreg::gen_dat_r)

# There is quite a bit that can go into documention.
# Review [Object Documentation](http://r-pkgs.had.co.nz/man.html) for more details.

# Eventually, you'll want to review the final documentation from build with working links.
# You'll also want to include a help for the overall package. That requires a file be added
# with just roxygen comments ended with *NULL* or *"_PACKAGE"*. This is typically also given the
# name of the package, thus [polyreg.R](../files/R/polyreg/R/polyreg.R)
if (getwd()=="/home/cdsw") {
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/polyreg.R",
    paste0(getwd(),"/R/polyreg/R/polyreg.R"),quiet = TRUE)
}
devtools::document("R/polyreg")
devtools::build("R/polyreg")
devtools::install("R/polyreg")
?polyreg
