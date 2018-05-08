# Vignettes, Different!

# To build a template vingette in CDSW:
system("rm -rf R/polyreg/vignettes")
devtools::use_vignette("beerbowl", pkg="R/polyreg")

# Again, this this creates a .gitignore file we don't need:
invisible(file.remove("R/polyreg/.gitignore"))

# So we'll want to overwrite the template with our own vignette 
if (tail(strsplit(getwd(),"/")[[1]],1)=="polyreg_build") {
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/vignettes/beerbowl.Rmd",
                "R/polyreg/vignettes/beerbowl.Rmd",quiet = TRUE)
}
file.edit('R/polyreg/vignettes/beerbowl.Rmd')


# You can also view using vignette after install
devtools::build_vignettes(pkg="R/polyreg")
devtools::document("R/polyreg")
devtools::build("R/polyreg")
devtools::install("R/polyreg")
vignette("beerbowl")