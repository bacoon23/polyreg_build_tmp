# # The Impact of Beer Consumption on Bowling Scores
#
# Let's reexamine the age old topic of [beer and bowling](http://bowlmovementswy.blogspot.com/2009/06/on-beer-and-bowling.html).
# A commonly held belief is that beer offers only a minimal, then diminishing 
# impact to a players score as drinking continues. A supporting observation of this 
# would be a plot indicating an increase then decrease in bowling average.
# To achieve this, we'll use the polyreg package and it's included data source, beerbowl.

library(polyreg)
?beerbowl
head(beerbowl)
plot_r(beerbowl)