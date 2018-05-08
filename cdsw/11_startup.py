# PYTHONSTARTUP
#
# [PYTHONSTARTUP](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP) is an
# environment variable used by python at the start of an interactive session. It is run
# in the same namespace as the eventual session so it is great for importing libraries
# you will need or in our case, modify the python path. I bring it up only to say we are
# not going to use it directly.

# Instead, we'll adopt [profiles](http://ipython.readthedocs.io/en/stable/config/intro.html#profiles).
# To create a default profile:
!ipython profile create

# This will create a few things beyond the scope of this tutorial. The folder we are 
# intersted in is the [startup](../files/.ipython/profile_default/startup/) folder
# within [profile_default ](../files/.ipython/profile_default/). *NOTE:* older versions
# used .config folder. We'll add a sys.path modification script into start up and then 
# explain why we did so:
import wget, shutil
url = 'http://github.mtv.cloudera.com/raw/mlop/polyreg/master/.ipython/profile_default/startup/00_startup.py'
out = '.ipython/profile_default/startup/00_startup.py'
f = wget.download(url,out)
shutil.move(f,out)

# The primary purpose of creating this startup file is to include
# [python](../files/python/) in sys.path. We want this so that as we iterate
# through our module changes so we can quickly run tests / verify change works.
f = open(out, 'r')
print f.read()
f.close()

# We'll of course need to stop this session and start a new one to be able to 
# see the desired effects on a new session
quit()