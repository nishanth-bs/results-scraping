from xml.dom import minidom
import requests
from bs4 import BeautifulSoup

student=requests.get('http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1rn15is055&sem=2').text
soup=BeautifulSoup(student,'html.parser')
names=soup.findAll("input",{"name":"txtName"})

for n in names:
    print (n['value'])




htmlstr = """    <input type="hidden" autocomplete="off" id="post_form_id" name="post_form_id" value="d619a1eb3becdc05a3ebea530396782f" />
...     <input type="hidden" name="fb_dtsg" value="AQCYsohu" autocomplete="off" />"""
>>> from BeautifulSoup import BeautifulSoup
>>> soup = BeautifulSoup(htmlstr)
>>> [(n['name'], n['value']) for n in soup.findAll('input')]
[(u'post_form_id', u'd619a1eb3becdc05a3ebea530396782f'), (u'fb_dtsg', u'AQCYsohu')]