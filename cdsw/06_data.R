# External Data
# It is cometimes a good idea to include data with your pakage. Not only
# for distributing data to broad audiences, but also to demonstrate use and 
# need for your packages functions.

# There are three ways to include data in your pacakge, but we'll only cover
# the first for our package:
# * 1) Store as binary in data/
# * 2) Store as parsed in R/sysdata.rda
# * 3) Store as raw, put in inst/extdata

# First, create a dataset. We'll fabricate ours, dummy data of handicap 
# bowling score and beer consumption. We'll include beer second and third
# powers so it matches our gen_dat_r format.
# **NOTE**: This is a completely fabricated data. Do not make life decisions 
# based upon what is presented here.
install.packages("triangle")
library("triangle")
gen_beerbowl <- function() {
  gen_dat    <- data.frame(x1=c(rtriangle(250,0,7,01.2),rep(0,250)))
  gen_dat$x2 <- gen_dat$x1^2
  gen_dat$x3 <- gen_dat$x1^3
  gen_dat$y  <- 191.6 + 11.55*gen_dat$x1 + -6*gen_dat$x2 + 0.4*gen_dat$x3 + rnorm(500,0,18)
  return(gen_dat[sample(nrow(gen_dat)),c("x1","x2","x3","y")])
}
beerbowl <- gen_beerbowl()
devtools::use_data(beerbowl,pkg="/home/cdsw/R/polyreg")

# ### Dcoumenting Datasets
# Yes, any time you include a dataset you should comment on metadata.
# We will again make use of roxygen comments. Since you can't really 
# document the data directly (like we did for functions), we'll create 
# a separate document. To make things easy, we'll copy
# existing code and save in our package R folder, [/home/cdsw/R/polyreg/R](../../rdev_build/files/R/polyreg/R/).

if (getwd()=="/home/cdsw") {
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/beerbowl.R",
    paste0(getwd(),"/R/polyreg/R/beerbowl.R"),quiet = TRUE)
}
devtools::document("/home/cdsw/R/polyreg")
devtools::load_all("/home/cdsw/R/polyreg")
head(polyreg::beerbowl)
?beerbowl