#!/usr/bin/env python
import sys


x=1
x+=1
print(str(x)+ ".... Look it works!")

print("Number of args:"+str(len(sys.argv)))
print("arg0: "+str(sys.argv[0]))
print("arg1: "+str(sys.argv[1]))



