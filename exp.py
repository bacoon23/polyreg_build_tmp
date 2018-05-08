#!/usr/bin/env python

import sys

# For testing iteration only, should be installed for prod
pack_dir='/home/cdsw/python'
if pack_dir not in sys.path:
  sys.path.append(pack_dir)

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.base import clone
#import matplotlib.pyplot as plt
from IPython.display import display, HTML
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', -1)
import polyreg.parser


# # ARGUMENTS
#------------
# Here are test arguments to mimic commandline or experiments call
#sys.argv=sys.argv[:1]
#sys.argv+=['--data', 'dat',
#           '--exp', 'polyreg.polylm',
#           '--hyper','{"lm__fit_intercept":False}',
#           '--cv', '{"cv":5}',
#           '--gs', '[{"poly__degree":[1,3],"poly__include_bias":[True,False]}]']


#a=args, mod=experiment module, dat=pandas df or spark df
a,mod,dat = polyreg.parser.parse(sys.argv[1:])

mdl=mod.mdl
y=dat.iloc[:,0]  # Note: response variable hard coded to first column

# # TRAIN
#--------

mdl=mdl.set_params(**a.hyper)

if a.cv != {}:
  cv_scores = cross_val_score(mdl,dat,y,**a.cv)
  print("cv scores: "+str(cv_scores))

if a.gs != {}:
  gscv = GridSearchCV(mdl, a.gs).fit(X=dat,y=y)
  rslt = pd.DataFrame({"params":[str(p) for p in gscv.cv_results_['params']],
            "score":gscv.cv_results_['mean_test_score']})[["score","params"]]\
            .sort_values("score",ascending=False).reset_index(drop=True)
  print("Model parameters set to highest Grid Search score:")
  print(rslt)
  #display(HTML(rslt.to_html(index=False)))
  mdl=mdl.set_params(**dict(a.hyper,**gscv.best_params_))

mdl=mdl.fit(dat,y)  

if a.save:
  print('TODO: save')

# # EXPLAIN
#----------
# Some type of graphic or vs baseline metric

mod.explain()


if True:
  col=mdl.get_params()['xSelect__col']
  dx = mdl.steps[0][1].transform(dat)
  pat=pd.DataFrame()
  pat[col] = [i for i in np.linspace(dx.min(), dx.max(), 120)]
  plt.scatter(dat[col], y,  color='black')
  plt.plot(pat[col], mdl.predict(pat), color='blue',linewidth=3)