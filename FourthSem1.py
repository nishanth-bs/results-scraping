import requests
import getthreedigit
from bs4 import BeautifulSoup
col=0


def vtu_results():
    url="http://results.vtu.ac.in/results/result_page.php" #"http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    flag=1
    '''1am14is062'''
    for yy in ['EE', 'CS', 'IS', 'ME', 'EI', 'EC', 'CV']:
        for e in range(1,200):
            if (yy==('EE'or'EI') and e==56)or(yy==('CS'or'IS') and e==127)or(yy=='ME' and e==171)or(yy=='EC'and e==177)or(yy=='CV' and e==65):
                break
            student = requests.get("http://results.vtu.ac.in/results/result_page.php?usn=1rn13is087").text   #url+str("?usn=1rn13")+yy+str(getthreedigit.digit(e))+str("&sem=7")).text
            soup = BeautifulSoup(student, "html.parser")
            namec = soup.findAll("input", {"name": "txtName"})
            for n in namec:
                print(n['value'])
            print("USN:1RN15"+yy + str(getthreedigit.digit(e)))

            for rows in soup.findAll('tr'):
                for columns in soup.findAll('td'):
                    for columns in soup.findAll('input', {"id": ("txtCP"+ str(i))}):
                        if (w==1):
                            namez = soup.findAll("input",{"id":"txtSub"+str(w)})
                            for l in namez:
                                print(l['value'],end="  :" )
                            print (columns['value'])
                        elif (w==2):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])
                        elif (w==3):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])
                        elif(w==4):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])
                        elif(w==5):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])
                        elif(w==6):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])
                        elif(w==7):
                            namez = soup.findAll("input", {"id": "txtSub" + str(w)})
                            for l in namez:
                                print(l['value'], end="  :")
                            print(columns['value'])

                        col= col + int(columns['value'])
                        w+=1
                        i+=1
                        if (i>7):
                            break
                    break
            w=1
            i=1
            print("Total Credits Earned  :" + str(col) + "\n\n")
            col = 0
vtu_results()