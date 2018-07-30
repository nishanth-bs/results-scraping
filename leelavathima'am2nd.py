import requests
import getthreedigit
from bs4 import BeautifulSoup
col=0


def vtu_results():
    url="http://results.vtu.ac.in/cbcs_17/result_page.php"#"http://result.vtu.ac.in/cbcs_results2017.aspx" #"http://result.vtu.ac.in/cbcs_results2016.aspx"
    col=0
    i=1
    w=1
    flag=1
    '''1am14is062'''
    for yy in [ 'CS']:#,'EC','EI','EE','CV']:#,'EE', 'ME', 'EI', 'EC', 'CV']:
        col=0
        for e in range(420,450):
            col=0
            '''if ((yy==('CS'or'IS') )):#and e==127)or yy==('EE'or'EI') and e==56)or(yy=='ME' and e==171)or(yy=='EC'and e==177)or(yy=='CV' and e==65):
                break'''
            student = requests.get(url+str("?usn=1rn16")+yy+str(getthreedigit.digit(e))).text
            soup = BeautifulSoup(student, "html.parser")
            namec = soup.findAll("td", {"style": "padding-left:15px"})
            print("1RN16" + yy + str(getthreedigit.digit(e)), end=",")
            for n in namec:
                print(n.get_text().replace(": ",""),end=",")


            #mark = soup.findAll("td")
            for rows in soup.findAll('tr'):
                i = 1
                j = 1
                mar =  []
                mark=0
                h = soup.findAll("td",{"style":"text-align:center;"})
                for columns in h:
                    i+=1

                    if(i%4==0):

                        mar =columns.get_text()
                        #if j==1 or j==2 or j==3 or j==4 or j == 5 or j==6:
                            #g= grade(int(mar))
                            #mark += g*4

                        #elif j==7 or j==8:
                            #g = grade(int(mar))
                            #mark += g*2
                        j+=1
                        if j>9:
                            break
                        else:
                            print(columns.get_text(),end=",")

                        #i=1
                    #print(columns.get_text())
                #f =float(mark)/28.00
                #print(mark)#,",","%.2f"%f)
                break


              #  j=0

            #   for i in range(0,2):
             #       print(mar[i],end="")
              #      j+=1
               #     if j%2==0:
                #        print()



                   # '''j+=1
                    #prev = i
                    #if(j%2==0):
                     #   print(str(prev)+str(i))
                    #    j=0'''





            print()


def grade(x):
    if(x >89):
        return 10
    elif(x>79):
        return 9
    elif x>69:
        return 8
    elif x>59:
        return 7
    elif x>49:
        return 6
    elif x>44:
        return 5
    elif x>39:
        return 4
    else:
        return 0


vtu_results()
