from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression

from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import PolynomialExpansion
from pyspark.ml.regression import LinearRegression

from ast import literal_eval

from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

from pyspark.ml import Pipeline

def get_spark():
  return(SparkSession.builder.appName("polyreg").getOrCreate())



vass = VectorAssembler(inputCols=["x",], outputCol="feat") 
poly = PolynomialExpansion(degree=3, inputCol="feat", outputCol="features")
lm   = LinearRegression(maxIter=5, regParam=0.0, solver="normal")

# Configure an ML pipeline
# Assignment by string to simplify the getParams() function
stages=["vass","poly","lm"]
pipe = Pipeline(stages=[eval(s) for s in stages])

def printParams():
  """Print method that will be called in parser script"""
  txt = "Model Pipeline Parameters:"
  for i in range(len(stages)):
    txt+= "\n Stage "+str(i).zfill(2)+": "+stages[i]
    pm=pipe.getStages()[i].extractParamMap()
    for p in pm.keys():
      txt+= "\n           "+stages[i]+"."+p.name+": "+str(pm[p])
  print(txt)

# First wonky difference here is that the parameters are actually the 
# transform objects, not string refrences to parameters (like in sklearn)
def eDict(d):
  """transform a dict of key strings into literal_eval keys"""
  return({eval(k):d[k] for k in d.keys()})

# Second wonky difference is that parameter grids are build as own instance
# not able to be passed as dicts (like in sklearn)
def build_ParamGrid(d):
  pgb=ParamGridBuilder()
  for k in d.keys():
    pgb.addGrid(eval(k),d[k])
  ParamGrid=pgb.build()  
  return(ParamGrid)



spark=get_spark()
dat  = spark.sql("SELECT y label, x1 x FROM polyreg.dat")

hyper={"lm.maxIter": 10, "poly.degree":3}
cv={"numFolds": 5}
gs={"poly.degree": [1,3]}

def train(dat,hyper,cv,gs):
  """standard training method arguement from experiment"""
  if gs != {}:
    



# Example of changes to hyper
#----
hyper={"lm.maxIter": 10, "poly.degree":3}

model = pipe.fit(dat, eDict(hyper))


# Example of changes to cv
#----
# Only the parameters related to 


cv={"numFolds": 5}



  
  
hyper={lm.maxIter: 10, poly.degree:3}

def build_ParamGrid():
  """Build a parameter grid from"""
  cvParamGrid = ParamGridBuilder() \
              .addGrid(lm.maxIter, [10, 20]) \
              .build()  



re = RegressionEvaluator()




crossval = CrossValidator(estimator=pipe,
              estimatorParamMaps=cvParamGrid,
              evaluator=re,
              **cv)

model = crossval.fit(dat)

# Example of changes to gs
#----
# Only the parameters related to grid are inclued.



model.stages[2].coefficients




paramMap.update({)  # Specify multiple Params.


# We may alternatively specify parameters using a Python dictionary as a paramMap
paramMap = {lr.maxIter: 20}
paramMap[lr.maxIter] = 30  # Specify 1 Param, overwriting the original maxIter.
paramMap.update({lr.regParam: 0.1, lr.threshold: 0.55})  # Specify multiple Params.

# You can combine paramMaps, which are python dictionaries.
paramMap2 = {lr.probabilityCol: "myProbability"}  # Change output column name
paramMapCombined = paramMap.copy()
paramMapCombined.update(paramMap2)

# Now learn a new model using the paramMapCombined parameters.
# paramMapCombined overrides all parameters set earlier via lr.set* methods.
model2 = lr.fit(training, paramMapCombined)
print("Model 2 was fit using parameters: ")
print(model2.extractParamMap())

model2.coefficients

test = spark.createDataFrame([
    (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
    (0.0, Vectors.dense([3.0, 2.0, -0.1])),
    (1.0, Vectors.dense([0.0, 2.2, -1.5]))], ["label", "features"])

prediction = model2.transform(test)
result = prediction.select("features", "label", "myProbability", "prediction") \
    .collect()

  
  



df = spark.createDataFrame([(Vectors.dense([0.5, 2.0]),)], ["dense"])


df = spark.createDataFrame([
  (1.0, 2.0, Vectors.dense(1.0)),
  (0.0, 2.0, Vectors.sparse(1, [], []))], ["label", "weight", "features"])





# Fit the pipeline to training documents.



qq=vat.transform(dat).head()
qq



qq = poly.transform(df).head()

>>> px = PolynomialExpansion(degree=2, inputCol="dense", outputCol="expanded")
>>> px.transform(df).head().expanded
DenseVector([0.5, 0.25, 2.0, 1.0, 4.0])
>>> px.setParams(outputCol="test").transform(df).head().test
DenseVector([0.5, 0.25, 2.0, 1.0, 4.0])
>>> polyExpansionPath = temp_path + "/poly-expansion"
>>> px.save(polyExpansionPath)
>>> loadedPx = PolynomialExpansion.load(polyExpansionPath)
>>> loadedPx.getDegree() == px.getDegree()
True  
  

  
  

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

# Prepare training documents from a list of (id, text, label) tuples.
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])  
  
  

from pyspark.sql import SparkSession
from pyspark.mllib.random import RandomRDDs
from pyspark.ml.linalg import Vectors
import pandas as pd
import numpy as np


def get_spark():
  return(SparkSession.builder.appName("polyreg").getOrCreate())

def gen_poly(x):
    x1 = float(x[0])
    x2 = float(np.power(x1,2))
    x3 = float(np.power(x1,3))
    X  = Vectors.dense(x1,x2,x3)  
    epsilon = float(x[1])
    y  = 4.0 + 6.0*x1 + 2.0*x2 - 1*x3 + epsilon
    return(y,X)

def gen_df_ml(sc=None,
              B=(4,6,2,-1),
              n=10000,
              rng=(-2,4),
              err=(0,4)):
  sc=get_sc() if sc is None else sc
  x1      = RandomRDDs.uniformRDD(spark, 10000).map(lambda x: np.diff(rng)*x+np.min(rng))
  epsilon = RandomRDDs.normalRDD(spark, 10000).map(lambda x: err[0]+err[1]*x)
  dat_df = x1.zip(epsilon).map(gen_poly)
  return(dat_df)



gen_df_sparklyr <- function(sc=get_sc(),
                      B=c(4,6,2,-1),
                      n=10000,
                      rng=c(-2,4),
                      err=c(0,4)) {
  dat<-gen_dat_r(B,n,rng,err)
  return(copy_to(sc, gen_dat_r(),"df",TRUE))
}









x1      = RandomRDDs.uniformRDD(spark, 10000).map(lambda x: 6.0*x-2)
epsilon = RandomRDDs.normalRDD(spark, 10000).map(lambda x: 4.0*x)
def gen_poly(x):
    x1 = float(x[0])
    x2 = float(np.power(x1,2))
    x3 = float(np.power(x1,3))
    X  = Vectors.dense(x1,x2,x3)  
    epsilon = float(x[1])
    y  = 4.0 + 6.0*x1 + 2.0*x2 - 1*x3 + epsilon
    return(y,X)
gen_dat = x1.zip(epsilon).map(gen_poly)

# ## Prepare Data as DataFrame
# This example will use the ML class which requires our data to be structured as a spark DataFrame.
# Well define our column for labels, y, and a column for feature vectors, X.

dat = spark.createDataFrame(gen_dat,["y", "X"])

# ## Train Model and Review Model Coefficients
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(featuresCol="X",labelCol="y")
lrModel = lr.fit(dat)

coef = pd.DataFrame(data=np.dstack((np.append(np.array([lrModel.intercept, ]), lrModel.coefficients), [4,6,2,-1]))[0])
coef.columns = ['ml_coef', 'true_coef']
coef