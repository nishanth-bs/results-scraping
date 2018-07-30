import requests
import getthreedigit
from bs4 import BeautifulSoup
col=0


def vtu_results():
    url="http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    flag=1

    for yy in [ 'CS','IS','ME','EC','EE','EI','CV']:
        for e in range(1,200):
            if (yy==('EE'or'EI') and e==56)or(yy==('CS'or'IS') and e==127)or(yy=='ME' and e==171)or(yy=='EC'and e==177)or(yy=='CV' and e==65):
                break
            student = requests.get(url+str("?usn=1rn15")+yy+str(getthreedigit.digit(e))+str("&sem=2")).text
            soup = BeautifulSoup(student, "html.parser")
            namec = soup.findAll("input", {"name": "txtName"})
            for n in namec:
                name=(n['value'])
                print(name.ljust(25,' '),end="")
            usn=("1RN15"+yy + str(getthreedigit.digit(e)))
            print(usn.center(15," "),end='')
            for rows in soup.findAll('tr'):
                for columns in soup.findAll('td'):
                    for columns in soup.findAll('input', {"id": ("txtCP"+ str(i))}):
                        if (w==1):

                            strrr=columns['value']
                            print(strrr.center(4,' '),end="")
                        elif (w==2):
                            strrr =  columns['value']
                            print(strrr.center(4, ' '), end="")


                        elif (w==3):
                            strrr =  columns['value']
                            print(strrr.center(4, ' '), end="")

                        elif(w==4):
                            strrr =  columns['value']
                            print(strrr.center(4, ' '), end="")

                        elif(w==5):
                            strrr =  columns['value']
                            print(strrr.center(4, ' '), end="")

                        elif(w==6):
                            strrr = columns['value']
                            print(strrr.center(4, ' '), end="")

                        elif(w==7):
                            strrr =  columns['value']
                            print(strrr.center(4, ' '), end="")


                        col= col + int(columns['value'])
                        w+=1
                        i+=1
                        if (i>7):
                            break
                    break
            w=1
            i=1
            maze= (col/24)
            strr=("GPA:" +str("%0.2f"%maze) )
            print(strr.center(10,' '))
            col = 0
vtu_results()