# # [Test Workflow](http://r-pkgs.had.co.nz/tests.html)
# Yes, we should automate tests.
# We recommend [testthat](https://github.com/r-lib/testthat). Getting started is easy.
devtools::use_testthat(pkg="/home/cdsw/R/polyreg/")

# **devtools::use_testthat** does a couple things:
# * Adds testthat to the DESCRIPTION Suggests field
# * Creates a [tests/testthat](../files/R/polyreg/test/testthat/) directory.
# * Creates [tests/testthat.R](../files/R/polyreg/test/testthat.R)

# To make things easy, we'll copy existing test code and save in our 
# [testthat](../files/R/polyreg/test/testthat/) folder.
if (getwd()=="/home/cdsw") {
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/tests/testthat/test-r.R",
    paste0(getwd(),"/R/polyreg/tests/testthat/test-r.R"),quiet = TRUE)
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/tests/testthat/test-sparklyr.R",
    paste0(getwd(),"/R/polyreg/tests/testthat/test-sparklyr.R"),quiet = TRUE)
}

# In general, the [Test Workflow](http://r-pkgs.had.co.nz/tests.html#test-workflow) becomes:
# * 1) Modify your [code](../files/R/polyreg/R/) or [tests](../files/R/polyreg/tests/testthat/)
# * 2) Run **devtools::test(<PATH>)**
# * 3) Repeat until all test pass

devtools::test(pkg="/home/cdsw/R/polyreg")

# You can see that the spark example took longer to test as expected.
# When you fix a bug, consider if a test is appropraite.