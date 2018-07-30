import re
pattern = input("Enter in the choice\n")
with open("dataasneededfinal.txt") as dataa:
    for lineno,line in enumerate(dataa):
        objectq= line.find("e")
        if (objectq==-1):
            break
        else:
            print(line)













    #    result=re.compile("\b n \d *s \b")
     #   if result.search(pattern)!=None:
      #      print("q")

