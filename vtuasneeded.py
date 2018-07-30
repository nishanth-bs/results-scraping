import requests
import getthreedigit
from bs4 import BeautifulSoup
col=0
def vtu_results():
    url="http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    for Z in ['EI','CV','EE','EC','IS','CS','ME']:

        for e in range(1,200):
            student = requests.get(url+str("?usn=1rn15")+Z+str(getthreedigit.digit(e))+str("&sem=2")).text
            soup = BeautifulSoup(student, "html.parser")
            print(Z+ str(getthreedigit.digit(e)), end=" ")


            for rows in soup.findAll('tr'):
                for columns in soup.findAll('td'):
                    for columns in soup.findAll('input', {"id": ("txtCP"+ str(i))}):
                        if (w==1):
                            print ((columns['value']), end=" ")
                        elif (w==2):
                            print((columns['value']), end=" ")
                        elif (w==3):
                            print(( columns['value']), end=" ")
                        elif(w==4):
                            print((columns['value']), end=" ")
                        elif(w==5):
                            print(( columns['value']), end=" ")
                        elif(w==6):
                            print(( columns['value']), end=" ")
                        elif(w==7):
                            print(( columns['value']), end=" ")

                        col= col + int(columns['value'])
                        w+=1
                        i+=1
                        if (i>7):
                            break
                    break
            w=1
            i=1
            print(str(col), end=" " )
            P = col / 24.00
            SGPA = ("%0.2f" % P )
            print(str(SGPA), end=" ")

            names = soup.findAll("input", {"name": "txtName"})
            for n in names:
                print(n['value'])
            col = 0







vtu_results()