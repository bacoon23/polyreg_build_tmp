from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from polyreg.data import gen_df

from sklearn.utils.validation import check_is_fitted

class xSelect(BaseEstimator, TransformerMixin):
    def __init__(self, col="x"):
        self.col = col
    def transform(self, X, **transform_params):
        trans = X[[self.col,]].copy() 
        return(trans)
    def fit(self, X, y=None, **fit_params):
        return(self)

mdl = Pipeline(steps=[('xSelect', xSelect(col="x")),
                      ('poly', PolynomialFeatures(degree=1)),
                      ('lm',   LinearRegression())])

def df3Xy(dat):
  """Parse"""
  return({"X":a.dat.drop(a.dat.columns[0],1),
          "y":a.dat.iloc[:,0]})


