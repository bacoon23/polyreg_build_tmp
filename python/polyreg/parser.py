import argparse
import json
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
from impala.dbapi import connect
import pickle
from pyspark.sql import SparkSession
import importlib
from ast import literal_eval

from IPython.core.display import display
from IPython.core.display import HTML


def get_dat(data, source):
  """get df (abstraction) for data & source provided
  
  depending data & source parameters provided, will determine correct pandas pf or spark
  data frame abstraction to return
  """
  # If source is not explicity provided, we'll infer the values
  # infered values are always

  
  source = None if source not in ["df","sdf","sql_impala","sql_spark","raw"] else source

  if source == None:
    try:
      dat = json.loads(data)
      source = "raw"
    except ValueError, e:
      sql = data if data[:6].lower()=="select" else "SELECT * FROM "+data
  
  if source == None:
    # first check if name is a path
    ls = [os.getcwd()+'/data/'+f for f in listdir('data')] + [os.getcwd()+'/'+f for f in listdir('.')]
    fs = []
    if '/' not in data:
      # not a full path, but may still be a file reference
      # check to see if has a file extension
      if '.' in data:
        fs = [f for f in ls if f.split("/")[-1]==data]   
      else:
        ext=["pkl","feather","csv"]
        fs = [f for f in ls if f.split("/")[-1].split(".")[0]==data and f.split("/")[-1].split(".")[-1] in ext]
    if len(fs) >= 1:
      # We have atleast one valid file path, we'll take the first
      source = "df"
      data = fs[-1]
    else:
      # We should now assume that the data componant provided is a table name or SQL
      #TODO figure out if sql_impala or sdf, etc.
      source="sql_impala"
      #source = "sdf"
      
  if source=="df":
    #TODO: add for more data sources (feather, csv), pickle only for now
    with open(fs[0], 'rb') as dat_pickle:
      dat = pickle.load(dat_pickle)
  
  if source in ["sdf","sql_spark"]:
    #TODO: Add conf handeling
    sc=SparkSession.builder.appName("parser").getOrCreate()
    dat=sc.sql(sql)
    
  if source=="sql_impala":
    # TODO: Make this so config it isn't hard coded
    conn = connect(host='bottou04.sjc.cloudera.com',
               port=21050,
               user='barker')
    cur = conn.cursor()
    cur.execute(sql)
    dat = as_pandas(cur)
    conn.close()
  
  print('\n')
  return(({"data":data,"source":source},dat))
    

def parse(args):

  #args=sys.argv[1:]
  
  # First figure out if we are dealing with commandline args or json
  parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("json",            type=str,help="json argument form")
  parser.add_argument("-d", "--data",    type=str, metavar='val',   help="path or sql of data source")
  parser.add_argument("-r", "--source",  type=str, metavar='src',   help="type of data source [df,sdf,sql_impala,sql_spark,raw]")
  parser.add_argument("-x", "--exp",     type=str, metavar='exp',   help="the experiment module name")
  parser.add_argument("-y", "--hyper",   type=str, metavar='{.}',   help="hyperparameters as json")
  parser.add_argument("-v", "--cv",      type=str, metavar='{.}',   help="cross validation as json")
  parser.add_argument("-g", "--gs",      type=str, metavar='{.}',   help="gridsearch parameters as json")
  parser.add_argument("-c", "--conf",    type=str, metavar='{.}',   help="spark config parameters as json")
  parser.add_argument("-q", "--quiet",   action="store_true",       help="supress argument parsing & parameter detail")
  parser.add_argument("-s", "--sas",     type=str, metavar='name',  help="model save as name")
  parser.add_argument("-S", "--save",    action="store_true",       help="save model, model name will be randomly generated")
  parser.description = """description: Call a single experiment with or without saving the results.
  Arguements can be passed as either commandline arguments or json.
  Compliant json provided for use in CDSW experiements UI.
  """
  
  # Change argumentless to help
  if (len(args)==0) or ('-h' in args) or ('--help' in args):
      return(parser.parse_args(['-h',]))
    
  # Add empty json if none exists
  x =  [i for i in args if i not in ["-h","--help","-S","--save","-q","--quiet"]]
  if 2*len([i for i in x if i[:1]=='-'])==len(x): 
      args.append('{}')
  
  # para is the parsed argument object we will enhance
  para = parser.parse_args(args)
  
  # Marry json and args (json overwrites args!)
  #para = parser.parse_args(['-d','data_test', '{"source":"source_test"}'])
  vars(para).update(json.loads(vars(para)['json']))
  del vars(para)['json']
  vars(para)['json'] = json.dumps(vars(para))
  
  # update data, source (ds) and retrieve dat
  ds,dat=get_dat(vars(para)['data'],vars(para)['source'])
  vars(para).update(ds)
  
  # retrieve experiment module
  # !! means all components specific to an anlysis are in a single module &
  # if multiple modules use the same experiment wrapper, they must have shared
  # methods !!
  mod=importlib.import_module(vars(para)['exp'])
  
  # Null to empty dict hyper / val / conf
  for a in ["hyper","cv","gs","conf"]:
    if vars(para)[a] is None:
      vars(para)[a] = {}
    else:
      if not isinstance(vars(para)[a],dict):
        vars(para)[a]=literal_eval(vars(para)[a])
  
  # If not quiet...
  if not para.quiet:
    # Argument Parsing & Parameter Detail:
    print("Parsed Arguments:")
    subj = {}
    for a in ["data","source","exp","hyper","cv","gs","conf","sas","save"]:
      if vars(para)[a] != {} and vars(para)[a] is not None and vars(para)[a] is not False:
        subj.update({a:vars(para)[a]})
        print(a.rjust(9)+": "+str(vars(para)[a]))
    print("\nArgument Resolved Objects:")
    print("dat: ".rjust(11)+str(dat.__class__))
    print("mod: ".rjust(11)+str(mod.__class__))  
    print("\nExperiments UI form:")  
    print(json.dumps(subj, indent=2, sort_keys=True))    
    if mod != None and hasattr(mod, 'mdl'):
      print("\nModel Pipeline Parameters:")
      kv = mod.mdl.get_params()
      for i,s in enumerate(mod.mdl.steps):
        p = s[0]+"__"
        print("  Step "+str(i).zfill(2)+": "+s[0])
        for k in [k for k in kv.keys() if p in k]:
          print("           "+k+": "+str(kv[k]))
      
  return((para,mod,dat))

print("http://spark.apache.org")