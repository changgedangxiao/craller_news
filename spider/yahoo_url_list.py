import requests
from bs4 import BeautifulSoup
import re
root_url="https://news.yahoo.com/"
resp=requests.get(root_url)
content=resp.content

soup=BeautifulSoup(content,"lxml")
url_list1=soup.find_all("h3",attrs={"class":"Mb(5px)"})
url_list=[]
for i in url_list1:
    i=unicode(i).encode("utf-8")
    ret=re.search(r'href="(.*).html',i)
    url="https://news.yahoo.com"+ret.group(1)+".html"
    url_list.append(url)
print url_list
print len(url_list)
