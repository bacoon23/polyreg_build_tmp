# # Python namespace and documentation

# TODO, make sure to update polyreg before blowing things away
# Now we have to actually write some code. To make things easy, we'll copy
# existing code and save in our python module folder, [/home/cdsw/R/polyreg/R](../../rdev_build/files/R/polyreg/R/)

#if (getwd()=="/home/cdsw") {
#  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/polyreg_r.R",
#    paste0(getwd(),"/R/polyreg/R/polyreg_r.R"),quiet = TRUE)
#  download.file("http://github.mtv.cloudera.com/raw/barker/polyreg/master/R/polyreg/R/polyreg_sparlyr.R",
#    paste0(getwd(),"/R/polyreg/R/polyreg_sparklyr.R"),quiet = TRUE)
#}

# If you inspect the code just loaded, you'll see we are using [docstrings](https://www.python.org/dev/peps/pep-0257/).
# **NOTE**: we have nothing against sphinx, but it is a little too much to take on as convention.
# Exisiting sphinx users will have no problem adapting this structure to fit thier needs.
with open('python/polyreg/polyreg_sklearn.py', 'r') as f:
    print f.read()

    
# Now that these files are loaded our namespace for python is self resolving
from polyreg import polyreg_sklearn
polyreg_sklearn
