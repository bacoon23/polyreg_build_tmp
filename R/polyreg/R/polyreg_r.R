#' Generate Data as DataFrame for Polynomial Regression
#'
#' @param B polynoimal coefficients, a number vector of length two or greater
#' @param n number of samples to generate
#' @param rng min and max of range to generate from as number vector length two
#' @param err mean and variance for normal distribution as noise to add to data set
#' @examples
#' dat <- gen_dat_r()
#' dat <- gen_dat_r(B=c(5,4,3,-2),n=4000,rng=c(-3,5),err=c(0,5))
#' @export
gen_dat_r <- function(B=c(4,6,2,-1),
                      n=10000,
                      rng=c(-2,4),
                      err=c(0,4)) {
  gen_dat    <- data.frame(x1=runif(n,rng[1],rng[2]))
  gen_dat$x2 <- gen_dat$x1^2
  gen_dat$x3 <- gen_dat$x1^3
  gen_dat$y  <- 4 + 6*gen_dat$x1 + 2*gen_dat$x2 - 1*gen_dat$x3 +  rnorm(n,err[1],err[2])
  return(gen_dat)
}

#' Generalized Linear Model for Polynomial Data
#'
#' @param dat DataFrame with response variable column named, 'y'
#' @export
glm_r <- function(dat=gen_dat_r()) {
  lm <- glm(y~.,data=dat)
  return(lm)
}

#' Plot Data and Fitted Model using stats::glm
#'
#' @param dat Polynomial Data
#' @param lm Linear Regression Fit on Polynomial Data
#' @examples
#' dat <- gen_dat_r(B=c(5,4,3,-2),n=4000,rng=c(-3,5),err=c(0,5))
#' lm  <- glm_r(dat=dat)
#' plot_r(dat,lm)
#' plot_r()
#' @export
plot_r <- function(dat=gen_dat_r(),lm=NULL) {
  if (is.null(lm)) {
    lm <- glm_r(dat)
  }
  rng=extendrange(dat$x1)
  pdat    <- data.frame(x1=seq(from = rng[1], to = rng[2], by = diff(rng)/120))
  pdat$x2 <- pdat$x1^2
  pdat$x3 <- pdat$x1^3
  pdat$y  <- predict(lm, pdat , interval = "prediction")

  plot(dat$x1,dat$y, xlab="x", ylab="y", main="Polynomial Regression using stats::glm")
  lines(pdat$x1,pdat$y,col="blue",lw=4)
}

