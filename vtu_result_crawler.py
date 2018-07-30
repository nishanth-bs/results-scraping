import requests
import getthreedif
from bs4 import BeautifulSoup

def vtu_homepage(max_pages):
    page=55
    while(page<=max_pages):
        url= "http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1rn15" + "is0" + str(page) + "&sem=2"
        results= requests.get(url)
        plain_text= results.text


        rows= tbody.find_all('tr')
        soup= BeautifulSoup(rows, "html.parser")
        for result in soup.findAll('td'):
            print (data)
        page+=1

vtu_homepage(55)