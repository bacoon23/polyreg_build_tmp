import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf





dates_df = pd.DataFrame({'dates': pd.date_range('2015-10-30', '2015-11-02')})

import numpy as np
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(poly)
X = np.array([[0, 1], [2, 3]])
transformer.transform(dat=dat)



def poly(dat=None, degree=3):
  dat=gen_df() if dat is None else dat
  name=dat.columns[1]
  for i in range(2,degree+1):
    dat[name+str(i)] = dat[name]**i
  dat=dat.rename(columns={name:name+"1"})





array([[ 0.        ,  0.69314718],
       [ 1.09861229,  1.38629436]])














dat = gen_df()




# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause


import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

logistic = linear_model.LogisticRegression()

pca = decomposition.PCA()
pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])



>>> from sklearn.pipeline import Pipeline
>>> from sklearn.svm import SVC
>>> from sklearn.decomposition import PCA
>>> estimators = [('reduce_dim', PCA()), ('clf', SVC())]
>>> pipe = Pipeline(estimators)
>>> pipe 
Pipeline(memory=None,
         steps=[('reduce_dim', PCA(copy=True,...)),
                ('clf', SVC(C=1.0,...))])




def poly(dat=none, degree=3):
  dat=gen_df() if dat is None else dat
  name=dat.columns[1]
  for i in range(2,degree+1):
    dat[name+str(i)] = dat[name]**i
  dat=dat.rename(columns={name:name+"1"})








results = smf.ols('y ~ .', data=gen_df()).fit()

print(results.summary())


degree=3

pd.Series(range(degree+1,1))


import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

results = smf.ols('y ~ x1 + x2 + x3', data=arg.dat).fit()
print(results.summary())


  
def lm_py(dat=None, degree=1):
  dat=gen_df() if dat is None else dat
  name=dat.columns[1]
  for i in range(2,degree+1):
    dat[name+str(i)] = dat[name]**i
  dat=dat.rename(columns={name:name+"1"})
  
  y ~ x1 + x2 + x3
  
  
  
  
  
  Y=Ymap.fit_transform(dat.copy())
  X=Xmap.fit_transform(dat.copy())
  regr = linear_model.LinearRegression(fit_intercept=True)
  regr.fit(X,Y)
  return(regr)


def plot_py(dat=None,regr=None):
  dat=gen_dat_py() if dat is None else dat
  regr=lm_py() if regr is None else regr
  x_range = np.array([[i,] for i in np.linspace(dat['x1'].min(), dat['x1'].max(), 100)])
  x_values = np.array([i[1:] for i in PolynomialFeatures(degree=3).fit_transform(x_range)])
  plt.scatter(dat['x1'], dat['y'],  color='black')
  plt.plot([i[0] for i in x_values], regr.predict(x_values), color='blue',linewidth=3)