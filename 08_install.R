# Because we are ussing a sub folder, installing using install_git requires subdir
devtools::install_git(url="http://github.mtv.cloudera.com/mlop/polyreg",subdir = "R/polyreg")

# Navigate through RStudio Help...
library(polyreg)
vignette("beerbowl")



