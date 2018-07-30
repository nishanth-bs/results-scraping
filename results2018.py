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
    resultBang = open('resultbang.txt','a')
    resultBang.write("INSERT INTO `student_marks`(`usn`, `name`, `subName1`, `sub1`, `sub1Pass`, `subName2`, `sub2`, `sub2Pass`,"
         " `subName3`, `sub3`, `sub3Pass`, `subName4`, `sub4`, `sub4Pass`, `subName5`, `sub5`, `sub5Pass`, `subName6`,"
         " `sub6`, `sub6Pass`, `subName7`, `sub7`, `sub7Pass`, `subName8`, `sub8`, `sub8Pass`, `subName9`, `sub9`, "
         "`sub9Pass`) VALUES ")
    ''''' print("INSERT INTO `student_marks`(`usn`, `name`, `subName1`, `sub1`, `sub1Pass`, `subName2`, `sub2`, `sub2Pass`,"
          " `subName3`, `sub3`, `sub3Pass`, `subName4`, `sub4`, `sub4Pass`, `subName5`, `sub5`, `sub5Pass`, `subName6`,"
          " `sub6`, `sub6Pass`, `subName7`, `sub7`, `sub7Pass`, `subName8`, `sub8`, `sub8Pass`, `subName9`, `sub9`, "
          "`sub9Pass`) VALUES")'''
    resultBang.close()
    for college in ('1as','1at','1au','1bg','1bt','1bc',
         '1bi','1bh','1bs','1bm','1by','1sk','1gg','1ic','1ki','1kn',
         '1me','1mj','1nj','1nc','1nh','1ox','1pn','1pe','1ri','1rl','1rr','1rg','1re','1rn','1sj','1va','1st','1sz',
         '1sg','1sc','1sp','1hs','1sb','1sv','1mv','1jb','1sw','1bn','1kt','1kh','1rc','1ve','1tj','1vi','1vj','1vk','1yd','1ap','1aa','1ao','1ah','1aj','1ak','1ac','1am'  ):
            #'4nn','4jn'):
         #'4gw','4jn','4kv','4km','4mh','4mt','4mk','4nn','4pa','4pm','4pr','4ra','4sf','4sh','4mw','4sm','4su','4sn',
         #'4es','4so','4ub','4vv','4vm','4vp','4yg'):#'1ay''1ar',
        #'1bo','1ck','1cr','1cd','1cg','1ce','1dt','1ds','1db','1da','1cc','1gv','1ec','1ep','1ew','1gs','1gc','1ga','1gd',
        #'1hk','1hm','1ii','1jv','1js','1jt','1ks','4al','4bw','4bb','4bd','4bp','4cb','4ci','4dm','4ek','4mg','4gm','4ge','4gh','4gl',
        #'4ad','4ai','4gk',

        #todo 4GLEC,4alcs,4glec,4mhis,4al17cs
        for dept in ('CS','EE','EC','CE','CH','EI','IM','TC','IS','BT','ME'):
            resultBang = open('resultbang.txt', 'a')
            checkCountStu = 0
            #file = open(college+dept,'a')
            #wb = xlwt.Workbook()
            #ws = wb.add_sheet('one')
            row = 1
            numbOfSubjects = 0
            excelfileheader = False
            for e in range(1,250):
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
                                    fileSub = open('subjectsList.txt','a')
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
                        resultBang.write("\n ,('")
                        resultBang.write(data['usn'].upper()+"'")
                        #file.write("\n"+data['usn'].upper())
                        #ws.write(row,col,data['usn'].upper())


                        col += 1
                        for columns in soup.findAll('td', {'style':'padding-left:15px'}):
                            resultBang.write(",'")
                            resultBang.write(columns.text[2:]+"'")
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
                                resultBang.write(",'")
                                resultBang.write(str(hashingSubjectsToNumb.get(columns.text,""))+"'")
                                #print("ggggggggggggggggggggg",columns.text)
                                #print("jjjjjjjjjjjjjjjj",hashingSubjectsToNumb)
                                subCodeItr += 1
                            if totalMarksStart +(marksItr -1)*6 is index:
                                resultBang.write(",'")
                                resultBang.write(columns.text+"'")
                                marksItr += 1
                            if passingStart +(passItr -1)*6 is index:
                                j+=1
                                resultBang.write(",'")
                                resultBang.write(columns.text+"'")
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
                            resultBang.write(",'','',''")
                            j += 1
                        resultBang.write(")")
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
            resultBang.close()
resultBang.close()
fileSub.close()