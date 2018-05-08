# # Reset CDSW Project (python 2 & 3)
# ... and install necessary packages

# There are some cdsw pip warnings I like to suppress so I do include a [pip.conf](../files/.config/pip/pip.conf)
# file for projects I'm working on in cdsw:

# TODO: the actual reset portion...
# ... since this needs to be saved to polyreg, we'll wait to write


# Users should be aware that pyspark is loaded from 
# /opt/cloudera/parcels/SPARK2/lib/spark2/python
# This works find at startup in cdsw becuase that path has been included in sys.path
import sys
sys.path

# However, this will cause issues when checking requirements becuase this package will 
# not been seen by pip or worse, could possibly trigger another install. As a cdsw hack when 
# working with requirements.txt in cdsw, I propose writing a folder to account
# for the modified sys.path and therefore no need to reload.
!mkdir -p /home/cdsw/.local/lib/python2.7/site-packages/pyspark-2.2.0.dist-info
!touch /home/cdsw/.local/lib/python2.7/site-packages/pyspark-2.2.0.dist-info/METADATA
!pip2 list | grep pyspark
!mkdir -p /home/cdsw/.local/lib/python3.6/site-packages/pyspark-2.2.0-py3.6.dist-info
!touch /home/cdsw/.local/lib/python3.6/site-packages/pyspark-2.2.0-py3.6.dist-info/METADATA
!pip3 list | grep pyspark

# Now, we won't... but we could have run the following for our dependencies:
# * !pip2 install pyspark==2.2.0
# * !pip2 install scikit-learn>=0.18.1
# * !pip3 install pyspark==2.2.0
# * !pip3 install scikit-learn>=0.18.1

# Instead, we'll capture all of our requirements in [requirements.txt](../files/python/requirements.txt)
# and run that instead:
!pip2 install wget
!pip3 install wget
import wget, shutil
url = 'http://github.mtv.cloudera.com/raw/mlop/polyreg/master/python/requirements.txt'
out = 'python/requirements.txt'
f = wget.download(url,out)
shutil.move(f,out)

!pip2 install -r python/requirements.txt
!pip3 install -r python/requirements.txt

# The pyspark site-packages folder changes made have no impact on the actual library
# loaded and simply mitigates warnings and errors when testing your requirements doc.
# See that pyspark is still read from the cloudera parcle:
import pyspark
pyspark.__file__

# **NOTE**: Not covered here & unnecessary for CDSW, users may prefer to use
# pipenv for thier local development. requirements.txt will not be impacted 
# by this choice.