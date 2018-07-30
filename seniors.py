import requests
from bs4 import BeautifulSoup

def vturesults():
    request= requests.get("http://results.vtu.ac.in/vitavi.php")
    soup=BeautifulSoup(request,"html.parser")
    for i in soup.findAll("input",{"name":"rid"}):
        i['value']=str(1rn15is055)