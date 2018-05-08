#' polyreg: a simple polynomial regression package
#'
#' Polynomial regression is a good demonstration of a statistical algorythm.
#' The resulting plot of randomly generated data can be shown in a cartesian
#' plane with a single predict curve to show users training works. Two methods
#' are employed, one local using \link[stats]{glm} and one using ml_linear_regression
#'
#' @section polyreg functions:
#' \itemize{
#'   \item \code{gen_dat_r}: generate a sample polynomial DataFrame
#'
#'   \item \code{glm_r}: train a polynomial model locally
#'
#'   \item \code{plot_r}: plot a polynomial scatter plot with predict curve
#'
#'   \item \code{gen_df_sparklyr}: generate a sample polynomial sparklyr DataFrame
#'
#'   \item \code{fit_sparklyr}: fit a polynomial model distributed
#'
#'   \item \code{plot_sparklyr}: plot a polynomial scatter plot with predict curve
#'
#' }
#'
#' @docType package
#' @name polyreg
"_PACKAGE"
