import requests
import getthreedigit
import os
from bs4 import BeautifulSoup
col=0
url="http://result.vtu.ac.in/cbcs_results2017.aspx"


def vtu_results():
     #"http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    flag=1
    '''1am14is062'''
    for yy in branches: #[ 'IS', 'CS']:#,'EE', 'ME', 'EI', 'EC', 'CV']:
        col=0
        for e in range(usn[0],usn[1]):#int(usn[0]),int(usn[1])):
            col=0
            '''if ((yy==('CS'or'IS') )):#and e==127)or yy==('EE'or'EI') and e==56)or(yy=='ME' and e==171)or(yy=='EC'and e==177)or(yy=='CV' and e==65):
                break'''
            student = requests.get(url+str("?usn=1rn16")+yy+str(getthreedigit.digit(e))+str("&sem=1")).text
            soup = BeautifulSoup(student, "html.parser")
            namec = soup.findAll("input", {"name": "txtName"})
            for n in namec:
                print(n['value'])
            print("USN:1RN16"+yy + str(getthreedigit.digit(e)))

            for rows in soup.findAll('tr'):
                for columns in soup.findAll('td'):
                    for columns in soup.findAll('input', {"id": ("txtCP"+ str(i))}):
                        if (w==1):
                            namez = soup.findAll("input",{"id":"txtSub"+str(w)})
                            for l in namez:
                                print(l['value'],end="                         :" )
                            a = columns['value']
                            print (a)
                        elif (w==2):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="                         :")
                            a=columns['value']
                            print(a)
                        elif (w==3):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="         :")
                            a = columns['value']
                            print(a)
                        elif(w==4):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="          :")
                            a = columns['value']
                            print(a)
                        elif(w==5):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="                :")
                            a = columns['value']
                            print(a)
                        elif(w==6):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="                           :")
                            a = columns['value']
                            print(a)
                        elif(w==7):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="                          :")
                            a = columns['value']
                            print(a)
                        elif (w == 8):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end=":")
                            a = columns['value']
                            print(a)

                        col= col + int(a)#int(columns['value'])
                        a=0
                        w+=1
                        i+=1
                        if (i>8):
                            break
                    break


            w=1
            i=1
            cred = str(col)
            print("Total Credits Earned                        :" + cred)
            sgpa = (float(cred)/240.000)*10.00
            print("SGPA----------------------------------------"+ "%.2f" % sgpa+ "\n\n")#round( String(cred/280),2))
            col = 0

print("The current fixed url is "+url )
if input(" \n To modify it press 1, else press any other key") ==1:
    url = input("\n Enter url")
branches = input('Enter branch or branches you wanna scrap results from separated by either spaces/commas/hyphen').split('' or ',' or '-')
usn = input('Enter the range of usn (eg:0-200').split(' ' and ',' and '-')
os.system('cls')
print('Requested results:')







vtu_results()