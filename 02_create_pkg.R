# We'll still need the following libraries in RStudio
install.packages(c('devtools','roxygen2','testthat','knitr'),quiet=TRUE)
install.packages(c("dplyr","sparklyr"),quiet=TRUE)

# In RStudio, there is a GUI for package creation... but, we'll still use devtools.

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
system("rm -rf R")
dir.create("R/polyreg",recursive=TRUE)
devtools::create("R/polyreg",description=description)

# This will create a bunch of files & we stull don't need polyreg.Rproj & .gitignore
invisible(file.remove("R/polyreg/.gitignore"))
invisible(file.remove("R/polyreg/polyreg.Rproj"))

# Finally, let's look at the files left and confirm our project [DESCRIPTION](../files/R/pkg/DESCRIPTION):
file.show('R/polyreg/DESCRIPTION')
