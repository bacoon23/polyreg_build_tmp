#' Get sc object if one exists
#'
#' If a variable sc exists, it is returned. If not, one is created using 
#' sparklyr::sparkconfig setting master to 'yarn-client'.
#' @export
#' @importFrom sparklyr spark_config
#' @importFrom sparklyr spark_connect
get_sc <- function() {
  if (!exists("sc")) {
    conf <- spark_config()
    sc <- spark_connect(master = "yarn-client", config = conf)
    assign("sc", sc, envir = .GlobalEnv)
  }
  return(sc)
}


#' Generate Data as DataFrame for Polynomial Regression
#'
#' @param B polynoimal coefficients, a number vector of length two or greater
#' @param n number of samples to generate
#' @param rng min and max of range to generate from as number vector length two
#' @param err mean and variance for normal distribution as noise to add to data set
#' @examples
#' df <- gen_df_sparklyr()
#' df <- gen_df_sparklyr(sc,B=c(5,4,3,-2),n=4000,rng=c(-3,5),err=c(0,5))
#' @export
#' @importFrom dplyr copy_to
gen_df_sparklyr <- function(sc=get_sc(),
                      B=c(4,6,2,-1),
                      n=10000,
                      rng=c(-2,4),
                      err=c(0,4)) {
  dat<-gen_dat_r(B,n,rng,err)
  return(copy_to(sc, gen_dat_r(),"df",TRUE))
}


#' Generalized Linear Model for Polynomial Data
#'
#' @param df sparklyr DataFrame with response variable column named, 'y'
#' @export
#' @importFrom sparklyr ml_linear_regression
fit_sparklyr <- function(df=gen_df_sparklyr()) {
  fit <- ml_linear_regression(df, y~.)
  return(fit)
}


#' Plot Data and Fitted Model using sparklyr::ml_linear_regression
#'
#' @param dat Polynomial Data
#' @param lm Linear Regression Fit on Polynomial Data
#' @examples
#' df <- gen_df_sparklyr(B=c(5,4,3,-2),n=4000,rng=c(-3,5),err=c(0,5))
#' fit <- fit_sparklyr(df=df)
#' plot_sparklyr(df,fit)
#' plot_sparklyr()
#' @export
#' @importFrom sparklyr %>%
#' @importFrom dplyr collect
#' @importFrom dplyr summarize
#' @importFrom sparklyr sdf_seq
#' @importFrom dplyr mutate
#' @importFrom dplyr select
#' @importFrom sparklyr sdf_predict
plot_sparklyr <- function(df=gen_df_sparklyr(),fit=NULL) {
  if (is.null(fit)) {
    fit <- fit_sparklyr(df)
  }
  dat <- df %>% collect
  rng <- df %>% summarize(min_x1 = min(x1,na.rm=TRUE),max_x1=max(x1,na.rm=TRUE)) %>% collect
  rng=extendrange(rng)
  incr<-diff(rng)/120
  pdat <- sdf_seq(sc, from = 1, to = 120, by = 1L, repartition = NULL) %>%
       mutate(x1 = rng[1]+id*incr) %>%
       mutate(x2 = x1^2) %>%
       mutate(x3 = x1^3) %>% 
       select(-id) %>%
       sdf_predict(fit) %>%
       collect
  plot(dat$x1,dat$y, xlab="x", ylab="y", main="Polynomial Regression using sparklyr::ml_linear_regression")
  lines(pdat$x1,pdat$prediction,col="orange",lw=4)
}
