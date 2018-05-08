# # Reset CDSW Project
# To make sure that R development build demo is set, we will:
# * Remove .Rprofile, R, .R
# * Create a clean R directory
# Yes, this will require you reinstall packages. This is a full reset.
#
# **Note**: Two folder exceptions, we will not remove/rebuild [cdsw](../files/cdsw/) or [RStudio](../files/RStudio)

system("rm -rf ~/.Rprofile ~/R ~/.R")
system("mkdir ~/R")

# We'll also quit this R session since it's possible .Rprofile ran.
quit("no")