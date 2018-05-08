


# # Let;s create some data to distribute with our library and to use in distributed examples




from polyreg.polyreg_sklearn import gen_dat_py
from impala.dbapi import connect
import pandas
reload(pandas)
import pandas as pd
from impala.util import as_pandas
import pickle

dat = gen_dat_py()


# put data into data as a pickle file
pickle.dump(dat, open( "data/dat.pkl", "wb" ) )


# Put data into hdfs / impala
dat.to_parquet('data/dat.parquet')

!hdfs dfs -mkdir /user/barker/polyreg
!hdfs dfs -mkdir /user/barker/polyreg/dat
!hdfs dfs -put data/dat.parquet /user/barker/polyreg/dat

conn = connect(host='bottou04.sjc.cloudera.com',
               port=21050,
               user='barker')
cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS polyreg LOCATION "/user/barker/polyreg"')
cur.execute('CREATE EXTERNAL TABLE IF NOT EXISTS polyreg.dat LIKE PARQUET "/user/barker/polyreg/dat/dat.parquet" STORED AS PARQUET LOCATION "/user/barker/polyreg/dat"')
cur.execute('USE polyreg')
cur.execute('SELECT * FROM polyreg.dat LIMIT 5')
cur.fetchall()
conn.close()

# Example snippet to download data from impala
conn = connect(host='bottou04.sjc.cloudera.com',
               port=21050,
               user='barker')
cur = conn.cursor()
cur.execute('SELECT * FROM polyreg.dat LIMIT 5')
dat = as_pandas(cur)
conn.close()

dat