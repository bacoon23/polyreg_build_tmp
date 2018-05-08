import json
import argparse
parser = argparse.ArgumentParser()
parser.parse_args(['test','--help'])



import json

json_data = '{"data": "value", "b": 2, "c": 3, "d": 4, "e": 5}'
json_data = '{"data": {"val":}, "b": 2, "c": 3, "d": 4, "e": 5}'

json.loads(json_data)["a"]

def parse(args=['dummy.py','--help']):
  # First figure out if we are dealing with commandline args or json
  
  
  parser = argparse.ArgumentParser()
  parser.add_argument("json", type=int,help="arguments as json")
  parser.add_argument("-s", "--save", action="store_true",
                    help="increase output verbosity")
  parser.add_argument("-S", "--save-as", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print "the square of {} equals {}".format(args.square, answer)
else:
    print answer
  
  
  
  
  
  
  
  
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True


json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, e: 5}'


json.loads(json_data)



# data {val:[string], src:[pickle,sdf,sql_impala,sql_spark]}
# trainer: string
# hyperparameters: {...}
# save:{save:yes, path:<string path>}







def parse(args=['dummy.py','--help']):
  
  
  
  
    parser = argparse.ArgumentParser()
    return(parser.parse_args(args))


parse()
  
  
import argparse



def parse()



import sys
sys.arg=['test','3','5','--sum']

parser = argparse.ArgumentParser(description='sum the integers at the command line')
parser.add_argument(
    'test', metavar='int', nargs='+', type=int,
    help='an integer to be summed')
parser.add_argument(
    '--log', default=sys.stdout, type=argparse.FileType('w'),
    help='the file where the sum should be written')
args = parser.parse_args(['test','3','5','--sum'])
args.log.write('%s' % sum(args.integers))
args.log.close()


