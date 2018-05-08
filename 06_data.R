# Data Workflow, same.
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
devtools::use_data(beerbowl,pkg="R/polyreg")

# Add some documentation
if (tail(strsplit(getwd(),"/")[[1]],1)=="polyreg_build") {
  download.file("http://github.mtv.cloudera.com/raw/mlop/polyreg/master/R/polyreg/R/beerbowl.R",
                "R/polyreg/R/beerbowl.R",quiet = TRUE)  
}


devtools::document("R/polyreg")
devtools::load_all("R/polyreg")
head(polyreg::beerbowl)
?beerbowl
