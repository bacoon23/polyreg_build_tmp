"""Collection of data generating functions for

As a means to simplify deployment. All data has been randomly


"""

import pyspark
import pandas as pd
import numpy as np


def get_sc():
  return(SparkSession.builder.appName("polyreg").getOrCreate())


def gen_df(B=(4,6,2,-1),
           n=10000,
           rng=(-2,4),
           err=(0,4)):
  x = np.array([[i,] for i in np.random.uniform(low=rng[0], high=rng[1], size=n)])
  y = B[0]+np.polyval(B[1:],x)+np.random.normal(err[0],err[1],size=[n,1])
  return(pd.DataFrame(np.column_stack((y,x)),columns=['y','x']))


def gen_sdf(sc=None,
            B=(4,6,2,-1),
            n=10000,
            rng=(-2,4),
            err=(0,4)):
  sc=get_sc() if sc is None else sc 
  rdm=pyspark.mllib.random.RandomRDDs
  x = rdm.uniformRDD(sc, n)\
      .map(lambda x: np.diff(rng)[0]*x+np.min(rng))
  e = rdm.normalRDD(sc, n)\
      .map(lambda x: err[0]+err[1]*x)
  sdf = x.zip(e)\
         .map(lambda x: (float(B[0]+np.polyval(B[1:],x[0])+x[1]),float(x[0])))
  return(sc.createDataFrame(sdf, ("y","x")))

# Code to write local copy:
# dat=gen_df()
# import pickle
# pickle.dump(dat, open( "data/dat.pkl", "wb" ) )

# Load copy to hdfs
# dat=gen_df()
# dat.to_parquet("dat.parquet")
# !hdfs dfs -rm /user/barker/polyreg/dat/dat.parquet
# !hdfs dfs -put dat.parquet /user/barker/polyreg/dat
# 