# # Reset CDSW Project
# To make sure that R development build demo is set, we will:
# * Remove .Rprofile, R, .R
# * Create a clean R directory
# Yes, this will require you reinstall packages. This is a full reset.
#
# **Note**: Two folder exceptions, we will not remove/rebuild [cdsw](../files/cdsw/) or [RStudio](../files/RStudio)
reset_package <- function(pack="polyreg_build") {
  if (tail(strsplit(getwd(),'/')[[1]],n=1)==pack) {
    system(paste0('rm -rf ',getwd(),'/R'))
    dir.create(paste0(getwd(),'/R'),recursive=TRUE)
  }
}

reset_package()
