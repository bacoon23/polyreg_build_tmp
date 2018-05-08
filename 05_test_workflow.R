# Test workflow, exactly the same, NOTE: shift+cmd+T
devtools::use_testthat(pkg="R/polyreg/")

# Copy existing testthat code
if (tail(strsplit(getwd(),"/")[[1]],1)=="polyreg_build") {
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/tests/testthat/test-r.R",
                "R/polyreg/tests/testthat/test-r.R",quiet = TRUE)
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/tests/testthat/test-sparklyr.R",
                "R/polyreg/tests/testthat/test-sparklyr.R",quiet = TRUE)
}

devtools::test(pkg="R/polyreg")

# Note, you'll get errors if sparklyr isn't configured