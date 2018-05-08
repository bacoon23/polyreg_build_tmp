# Now we have to actually write some code. To make things easy, we'll copy existing code
if (tail(strsplit(getwd(),"/")[[1]],1)=="polyreg_build") {
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/R/polyreg_r.R",
                "R/polyreg/R/polyreg_r.R",quiet = TRUE)
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/R/polyreg_sparlyr.R",
                "R/polyreg/R/polyreg_sparklyr.R",quiet = TRUE)
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/R/polyreg.R",
                "R/polyreg/R/polyreg.R",quiet = TRUE)
}

# devtools::document has a keyboard hortcut shift+cmd+D
devtools::document("R/polyreg")
file.show("R/polyreg/NAMESPACE")

# devtools::load_all has a keyboard shortcut shift+cmd+L
devtools::load_all("R/polyreg")
polyreg::plot_r()