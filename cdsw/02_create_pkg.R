# # Create R Package polyreg
# When deleveloping packages in R, we recommend being familiar with the
# the developer conventions practices by [Hadley Wickham](http://hadley.nz/).
# A very good reference book for his developer pactices and his developer
# library is [R Packages](http://r-pkgs.had.co.nz/).

# The following developer libraries, which will now be saved in .R
install.packages(c('devtools','roxygen2','testthat','knitr'),quiet=TRUE)
system("ls -l /home/cdsw/.R")

# Knowing that we are going to write a library that imports dplyr & sparklyr...
install.packages(c("dplyr","sparklyr"),quiet=TRUE)

# **NOTE**: We do not recommend [package.skeleton()](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/package.skeleton.html)

# Using devtools, we can set out global package developer options:
options(devtools.name="Brad")
options(devtools.desc.author='person("Brad", "Barker", email = "barker@cloudera.com", role = c("aut", "cre"))')
options(devtools.desc.license="GLP-2")

# We'll also create a description list specific to this package:
description <- list(
  Package="polyreg",
  Title="Polynomial Regression using Sparklyr",
  Description="Methods to generate data and train polynomial regression models.",
  Imports="dplyr, sparklyr"
)

# Using our global defaults and description, we'll create our project:
system("rm -rf ~/R")
dir.create("/home/cdsw/R/polyreg",recursive=TRUE)
devtools::create("/home/cdsw/R/polyreg",description=description)

# This will create a bunch of files:
# * [DESCRIPTION](../files/R/polyreg/DESCRIPTION) -  Important metadata about your package
# * [NAMESPACE](../files/R/polyreg/NAMESPACE) - Handles import/export declarations for your package
# * [R](../files/R/polyreg/R/) - package code folder
# * [.Rbuildignore](../files/R/polyreg/.Rbuildignore) - prevents files inclusion in bundled package

# There was actually two more files created which we won't need since this is not
# our project home directory:
invisible(file.remove("/home/cdsw/R/polyreg/.gitignore"))
invisible(file.remove("/home/cdsw/R/polyreg/polyreg.Rproj"))


# Finally, let's look at the files left and confirm our project [DESCRIPTION](../files/R/pkg/DESCRIPTION):
system("ls -a /home/cdsw/R/polyreg")
invisible(file.show('/home/cdsw/R/polyreg/DESCRIPTION'))