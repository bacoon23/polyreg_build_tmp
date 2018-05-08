#' beerbowl
#'
#' A completely fictitious data set of handicap adjusted bowling scores from 
#' the never-happened Cincinnati Bowling Extravaganza, 1988. This data set includes
#' randomly generated data from 500 individuals during the made-up event weekend.
#' Of the 500 participants, 250 did not drink during the event. Non-drinkers
#' were not excluded from beer frame obligations, but may have elected a
#' non-beer drink from a beer frame windfall.
#'
#' @format dataframe in polyreg format 
#' \itemize{
#'   \item \code{y}: representing the handicap adjusted weekend score
#'
#'   \item \code{x1}: average number of beers consume over 30 frames for the 
#'   duration of the extravaganza
#'
#'   \item \code{x2}: x1 squared
#'
#'   \item \code{x3}: x1 cubed
#'
#' }
"beerbowl"
