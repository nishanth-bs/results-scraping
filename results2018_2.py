import requests
import getthreedigit
import xlwt
#import mysqldb
#import xlsxwriter
from bs4 import BeautifulSoup
#import bs4
flag = True
hashingSubjectsToNumb = {}
hashingSubjectKeyCount = 0
while(flag):
    print("INSERT INTO `student_marks`(`usn`, `name`, `subName1`, `sub1`, `sub1Pass`, `subName2`, `sub2`, `sub2Pass`,"
          " `subName3`, `sub3`, `sub3Pass`, `subName4`, `sub4`, `sub4Pass`, `subName5`, `sub5`, `sub5Pass`, `subName6`,"
          " `sub6`, `sub6Pass`, `subName7`, `sub7`, `sub7Pass`, `subName8`, `sub8`, `sub8Pass`, `subName9`, `sub9`, "
          "`sub9Pass`) VALUES")
    for college in (#'2av','2ag','2ab','2ae','2bv','2bl','2gp','4go','2gb','2hn','2ji',
         #'2kd','2ke','2kl','2gi','2mb','2mm','2rh','2bu','2sr','2sa','2ha','2ka','2tg','2vs','2vd',
         #'3bk','3br',
         '1rn','3gf'):#3gf','3gu','3gn','3kc','3kb','3la','3na','3pg','3vc','3rb','3sl','3vn'):
        #'3ae',
        for dept in ('CV','CS','EC','IS','CH','EI','IM','TC','EE','BT','ME'):
            checkCountStu = 0
            #file = open(college+dept,'a')
            #wb = xlwt.Workbook()
            #ws = wb.add_sheet('one')
            row = 1
            numbOfSubjects = 0
            excelfileheader = False
            for e in range(1,200):
                numb = e
                col = 0
                row += 1
                while True:
                    try:
                        data= {
                            'usn': str(college)+'17'+str(dept)+str(getthreedigit.digit(numb))
                        }
                        url =  "http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"
                        #print(data,college)
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
                                    fileSub = open('subjectsList6.txt','a')
                                    fileSub.write(str("INSERT INTO `subjects`(`sub_id`, `subName`) VALUES ('").strip()+str(hashingSubjectKeyCount)+
                                                  "','".strip()+str(sub.text)+str("')").strip()+";\n")
                                    fileSub.close()

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
                        print(data['usn'].upper(),end="'")
                        #file.write("\n"+data['usn'].upper())
                        #ws.write(row,col,data['usn'].upper())


                        col += 1
                        for columns in soup.findAll('td', {'style':'padding-left:15px'}):
                            print(end=",'")
                            print(columns.text[2:], end="'")
                            #file.write(columns.text+",")
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
                                print(str(hashingSubjectsToNumb.get(columns.text,"")),end="'")
                                #print("ggggggggggggggggggggg",columns.text)
                                #print("jjjjjjjjjjjjjjjj",hashingSubjectsToNumb)
                                subCodeItr += 1
                            if totalMarksStart +(marksItr -1)*6 is index:
                                print(",'",end="")
                                print(columns.text,end="'")
                                marksItr += 1
                            if passingStart +(passItr -1)*6 is index:
                                j+=1
                                print(",'",end="")
                                print(columns.text,end="'")
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

                        while (j < 9):
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
                        for x in range(0,1000):
                            pass
                        continue
                    break
                if checkCountStu > 10: #if more than 10 empty records found, consider that branch has no more students
                    break
fileSub.close()