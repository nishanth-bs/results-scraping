import requests
import getthreedigit
#import xlwt
#import mysqldb
#import xlsxwriter
from bs4 import BeautifulSoup
#import bs4
flag = True
hashingSubjectsToNumb = {}
hashingSubjectKeyCount = 0
url = "http://results.vtu.ac.in/vitaviresultcbcs2018/resultpage.php"
while(flag):
    for college in ('1rn',):
        for dept in ('IS','CS'):#,'EE','EC','CE','CH','EI','IM','TC','CS','BT','ME'):

            #hashingSubjectsToNumb =   {'15MAT41': 1, '15CS42': 2, '15CS43': 3, '15CS44': 4, '15CS45': 5, '15CS46': 6, '15CSL47': 7, '15CSL48': 8, 'Subject Code': 9, '15MAT31': 10, '15CS32': 11, '15CS33': 12, '15CS34': 13, '15CS35': 14, '15CS36': 15, '15CSL37': 16, '15CSL38': 17, '15MAT21': 18, '15PCD23': 19, '15PHY12': 20, '15ELE15': 21}

            checkCountStu = 0
            file = open(college+dept,'a')
            row = 1
            numbOfSubjects = 0
            excelfileheader = False
            for e in range(400,450):
                numb = e
                col = 0
                row += 1
                while True:
                    try:
                        data= {
                            'lns': str(college)+'16'+str(dept)+str(getthreedigit.digit(numb)),
                            'token':'bHFKSWRvQ2MyWGtuT2hmS1pWbDNvMVNVdTBxOFN1aGJrck5JMGRJampUanFkaEtLYmRlN0c0ME5FdUFnM0RhVzNsZStLU2J5TjM4dFJxcE1EbXl6Q0E9PTo6+8nqZWm4ShQ8dP0Ll6M2MQ==',
                            'current_url':'http://results.vtu.ac.in/vitaviresultcbcs2018/index.php'
                        }
                        source_code = requests.post(url,data=data).text
                        #print(source_code)
                        soup = BeautifulSoup(source_code,"html.parser")
                        checkCount = 0
                        subNumbInTable = 2 #formula 1+(n-1)6
                        b = 0
                        for sub in soup.findAll('div', {'class': 'divTableCell'}):
                            subNumb = 1 + (subNumbInTable-1)*6
                            b += 1
                            if b is subNumb:
                                subNumbInTable += 1
                                if (sub.text not in hashingSubjectsToNumb.keys()) and (sub.text != str('P -> PASS')):
                                    hashingSubjectKeyCount += 1
                                    hashingSubjectsToNumb[sub.text] = hashingSubjectKeyCount
                                    print("#",hashingSubjectsToNumb)
                        #print(hashingSubjectsToNumb)
                        if(not excelfileheader):
                            excelfileheader = True
                            #ws.write(0,0,'NAME')
                            #ws.write(0,1,'USN')

                            index=2
                            for x in soup.findAll('div',{'style':'text-align: left;width: 400px;'}):
                                numbOfSubjects += 1
                                #ws.write(0,index,x.text)
                                index += 2

                        for check in soup.findAll('div',{'class':'divTableCell'}):
                            checkCount += 1
                        if(checkCount<10):  #check if the table is present in the result page, i.e if the usn is valid
                            checkCountStu += 1
                            break
                        print("\n ,('", end="")
                        print(data['lns'].upper(),end="'")
                        file.write("\n"+data['lns'].upper())
                        col += 1
                        for columns in soup.findAll('td', {'style':'padding-left:15px'}):
                            print(end=",'")
                            print(columns.text[2:], end="'")
                            file.write(columns.text+",")
                            #ws.write(row,col,columns.text[2:])
                        i=0
                        j=0
                        col += 1
                        subCodeStart = 7
                        totalMarksStart = 11
                        passingStart = 12
                        index = 0
                        subCodeItr = 1
                        marksItr = 1
                        passItr =1
                        resultlist = [0] * 20
                        gradelist = [0] * 20
                        for columns in soup.findAll('div',{'class':'divTableCell'}):
                            index += 1
                            if (j ==  numbOfSubjects):
                                print("",end="")
                                break
                            #print(columns.text)
                            if subCodeStart +(subCodeItr-1)*6 is index:
                                #if str(hashingSubjectsToNumb.get(columns.text)) == 'None':
                                   # break
                                print(",'",end="")
                                ind = hashingSubjectsToNumb.get(columns.text,"")

                                #print(str(hashingSubjectsToNumb.get(columns.text,"")),end="'")
                                #print(hashingSubjectsToNumb)
                                subCodeItr += 1
                            if totalMarksStart +(marksItr -1)*6 is index:
                                #print(",'",end="")
                                #print(columns.text,end="'")
                                try:

                                    resultlist[ind] = columns.text
                                except:
                                    pass
                                marksItr += 1
                            if passingStart +(passItr -1)*6 is index:
                                j+=1
                                #print(",'",end="")
                                #print(columns.text,end="'")
                                try:

                                    gradelist[ind] = columns.text
                                except:
                                    pass
                                passItr += 1
                            '''if not columns:
                                print("breaking out")
                                break'''
                            #print(columns)
                            '''i += 1

                            if(j == 2*numbOfSubjects):
                                break
                            if(i==11 or i==0):
                                print(columns.text, end=",")
                                #file.write(columns.text+",")
                                try:
                                    val = int(columns.text)
                                    ws.write(row, col, val)
                                    j+=1
                                except ValueError:
                                    ws.write(row, col, columns.text)
                                    j+=1
                                col +=1
                                if(i==11):
                                    i=-1
                                if(i==0):
                                    i=6

                            #wb.save(college+dept+'mmmm.xls')
                        if(college == '1ap' and e == 199):
                            flag = False
                        #print (source_code)'''
                        try:
                            for i in range(len(gradelist)):
                                print(resultlist[i],",",gradelist[i],",",end="")
                        except:
                            pass
                        while (j < 15):
                            print(",'','',''", end="")
                            j += 1
                        print(")", end="")
                    except requests.exceptions.Timeout as e:
                        #print(e +"TIMEOUT")
                    # Maybe set up for a retry, or continue in a retry loop
                        for x in range(0,1000):
                            pass
                        continue
                    except requests.exceptions.TooManyRedirects as e:
                        #print(e+"TOO ")
                    # Tell the user their URL was bad and try a different one
                        for x in range(0,1000):
                            pass
                        continue
                    except requests.exceptions.RequestException as e:
                        #print(str(e)+"RequestException")
                    # catastrophic error. bail.
                        for x in range(0,100):
                            pass
                        continue
                    break
                #if checkCountStu > 10: #if more than 10 empty records found, consider that branch has no more students
                 #   break
#fileSub.close()
