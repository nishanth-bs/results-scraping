import re

pattern= input("Enter a pattern")
with open ("dataasneededfinal.txt","r") as file:
    for lineno, line in enumerate(file):
        string=line
        a=string.find(pattern,5)
        if(a is not -1):
            print(a)