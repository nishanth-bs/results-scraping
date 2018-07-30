import requests
import getthreedigit
from bs4 import BeautifulSoup
col=0
def vtu_results():
    url="http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    for Z in ['ME','IS','CS']:

        for e in range(80,200):
            student = requests.get(url+str("?usn=1rn15")+Z+str(getthreedigit.digit(e))+str("&sem=2")).text
            soup = BeautifulSoup(student, "html.parser")
            print("USN:1RN15" +Z+ str(getthreedigit.digit(e)))

            names = soup.findAll("input", {"name": "txtName"})
            for n in names:
                print(n['value'])

            for rows in soup.findAll('tr'):
                for columns in soup.findAll('td'):
                    for columns in soup.findAll('input', {"id": ("txtCP"+ str(i))}):
                        if (w==1):
                            print ("Mathematics:"+columns['value'])
                        elif (w==2):
                            print("Chemistry:" + columns['value'])
                        elif (w==3):
                            print("PCD:" + columns['value'])
                        elif(w==4):
                            print("CAED:" + columns['value'])
                        elif(w==5):
                            print("Electronics:" + columns['value'])
                        elif(w==6):
                            print("Comp Programming Lab:" + columns['value'])
                        elif(w==7):
                            print("Chemistry Lab:" + columns['value'])

                        col= col + int(columns['value'])
                        w+=1
                        i+=1
                        if (i>7):
                            break
            w=1
            i=1
            print("Total Credits Earned=" + str(col) )
            P = col / 24.00
            SGPA = ("%0.2f" % P )
            print("SGPA:" + str(SGPA)+ "\n\n")
            col = 0







vtu_results()