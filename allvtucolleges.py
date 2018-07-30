import requests
from bs4 import BeautifulSoup

url = "http://www.fastvturesults.com/college_codes"
html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")
i=0
for columns in soup.findAll("td"):
    i+=1
    if(i==3):
        print("'",end="")
        print(columns.text , end="',")
        i=0
#print(html)