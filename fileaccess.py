import re
#with open("vturesultsfinal.txt","r") as f:
 #  # for line in f:
  ##      x=line
     ##   if (x=='\n'):
         #   if (x=='\n'):
       ##     continue
        #elif (x[-2:-1]=='\n'):

           # continue
        ##print (x)
#f=open('dataasneededfinal.txr','r')
import sys
import fileinput
with open("pranavasked.txt","r") as f:
  #  if line.rstrip():
   #         print (line)#
    for line in f:
        if not line.isspace():
            sys.stdout.write(line)
