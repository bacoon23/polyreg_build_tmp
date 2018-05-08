import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import LabelEncoder as enc
from sklearn_pandas import DataFrameMapper
import matplotlib.pyplot as plt
import pprint as pp

from sklearn.base import TransformerMixin

from sklearn.model_selection import cross_val_score?

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


# Reference Material
# https://medium.com/bigdatarepublic/integrating-pandas-and-scikit-learn-with-pipelines-f70eb6183696

def gen_df(B=(4,6,2,-1),
           n=5,
           rng=(-2,4),
           err=(0,4)):
  x = np.array([[i,] for i in np.random.uniform(low=rng[0], high=rng[1], size=n)])
  y = B[0]+np.polyval(B[1:],x)+np.random.normal(err[0],err[1],size=[n,1])
  return(pd.DataFrame(np.column_stack((y,x)),columns=['y','x']))

dat = gen_df()

pipe = Pipeline(steps=[('poly', PolynomialFeatures(degree=1)),
                       ('lm',   LinearRegression())])

conf={"poly__degree":2,"poly__include_bias":False}



pipe.set_params(**conf) 

X = np.array([[ 0.07104879],
              [ 1.18651216],
              [ 2.63051303],
              [-0.69116347],
              [-1.22442243]])


y = np.array([-0.4783423 ,
              8.30049868,
              12.75895714,
              -2.85814978,
              3.33808593])

pp.pprint(pipe.fit(X=X, y=y))

pp.pprint(pipe.get_params())

pipe.predict(X)














Ymap = DataFrameMapper([(['y',], StandardScaler(with_mean=False, with_std=False)),])
Xmap = DataFrameMapper([(['x1','x2','x3'], StandardScaler(with_mean=False, with_std=False)),])

def gen_dat_py(B=(4,6,2,-1),
               n=10000,
               rng=(-2,4),
               err=(0,4)):
    x1 = np.array([[i,] for i in np.random.uniform(low=rng[0], high=rng[1], size=n)])
    X = PolynomialFeatures(degree=3).fit_transform(x1)
    X = np.array([i[1:] for i in X])
    calc_y  = lambda x: B[0] + B[1]*x[0] + B[2]*x[1] + B[3]*x[2] + np.random.normal(err[0],err[1])
    Y = np.apply_along_axis(calc_y, 1, X)
    return(pd.DataFrame(data= np.c_[X,Y],columns=["x1","x2","x3","y"]))

  
def lm_py(dat=None):
  dat=gen_dat_py() if dat is None else dat
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
  