# # .Rprofile & Folders
# In cdsw there are convention conflicts caused by using /home/cdsw as:
#  * cdsw user home folder
#  * R_LIB_USER parent folder
#  * git project root folder

# **First**: To avoid putting scripts cdsw scripts in project root, we'll
# write all cdsw scripts in [/home/cdsw/cdsw](../files/cdsw/) as this script is already.

# **Second**: We'd prefer to use the git project folder R for R scripts. This
# is consistent with other apache projects like [Spark](https://github.com/apache/spark/tree/master/R).
# However, the folder **/home/cdsw/R** is already in use by R_LIB_USER. As a work a
# workaround until alignment on proper use, we'll use .Rprofile to deconflict.
# The .Rprofile create yes another convention for user lib which works well
# for our immediate purposes.
#  * CRAN R User Lib Convention: **~/R/R.version$platform-library/x.y**
#  * CDSW R User Lib Convention: **~/R**
#  * Proposed .Rprofile CDSW R User Lib Convention: **~/.R**

# Let's copy the file from [rdev](http://github.mtv.cloudera.com/barker/rdev/blob/master/.Rprofile) and have a look.
if (getwd()=="/home/cdsw") {
  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/.Rprofile","/home/cdsw/.Rprofile",quiet = TRUE)
}
invisible (file.show('/home/cdsw/.Rprofile'))

# So that installs can actually take place in our new R_LIB_USER setting:
dir.create('/home/cdsw/.R')

# **NOTE**: There are lookups that occur in **~/.R** for environ(.site) files.
# This does not create a conflict since we would never conflict with the existing
# CDSW environ(.site) files and this lib folder convention is specific to CDSW
# sessions.

# **NOTE**: None of this is really necessary with local or server RStudio. That
# is why we check for the condition that we are in a CDSW Session

# **NOTE**: This will conflict with R developers practice of keeping the
# working directory the same as project root. However, it complicates script
# references to have a practice of setwd(), so I do not recommend using it in
# cdsw.

# Here are other start-up scripts but none are impacted by these changes.
# No action, just aware of your CDSW configs:
invisible(file.show('/usr/local/lib/R/etc/Renviron'))
invisible(file.show('/etc/R/Rprofile.site'))
Sys.getenv("R_PROFILE") 

# Since **R_PROFILE** is unset, <PWD>/.Rprofile is called; the effect we want.

# So that the effects of .Rprofile take place we'll and quit this R session.
# Future sessions that *install.packages* will save those packages into .R.
quit('no')
