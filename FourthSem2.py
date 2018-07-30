import requests
from bs4 import BeautifulSoup

branches = open("Departments", "r")
# branches.split(",")

#for i in range(0,2):#branches:
    #j = i.split(",")
    # for k in j:

webPage = requests.get("http://results.vtu.ac.in/results/result_page.php?usn=1rn13is087").text
soup = BeautifulSoup(webPage, "html.parser")
#for i in soup.findAll("tr"):
for j in soup.findAll("td",{"style":"padding-left:15px"},text=True):
    print (j)

webPage = requests.get("http://results.vtu.ac.in/results/result_page.php?usn=1rn13cs087").text
soup = BeautifulSoup(webPage, "html.parser")
#for i in soup.findAll("tr"):
for j in soup.findAll("td",{"style":"padding-left:15px"}):
    print (j)

'''name = soup.findAll("tr", {"style":"height:35px"})
#namec = name.findAll("td",{"style":"padding-left:15px"})
for n in name:
    print(n)
'''