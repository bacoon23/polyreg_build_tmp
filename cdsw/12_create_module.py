# Create Python Project

# We'll want to create the following files. They deserve more explaination than
# what is provided here, so check out [distributing packages](https://packaging.python.org/tutorials/distributing-packages/).
# * [README.rst](../files/python/README.rst) - README for python package of polyreg
# * [setup.py](../files/python/setup.py)
# * [MANIFEST.ini](../files/python/MANIFEST.ini)

# **NOTE**: If you look in setup.py, you will see that we are using [setuptools](https://github.com/pypa/setuptools)
# instead of [distutils](https://docs.python.org/3/library/distutils.html). This is a
# package decision that could be challeneged by a customer. If they have an alternate 
# convention already present, adapt to existing convention as reasonable.

import wget, shutil
for i in ['README.rst','setup.py','MANIFEST.ini']:
  url = 'http://github.mtv.cloudera.com/raw/mlop/polyreg/master/python/{0}'.format(i)
  out = 'python/{0}'.format(i)
  f = wget.download(url,out)
  shutil.move(f,out)
  
# We'll also need the code folder, which is called by the project name:
!mkdir -p python/polyreg

# However, we are still not able to import 
import polyreg

# Becuase for the folder to be identified as a module you have to include an __init__.py file
!touch python/polyreg/__init__.py
import polyreg

# Ok sure, there is nothing there to actually run so we'll have to add some files:
command_line.py











