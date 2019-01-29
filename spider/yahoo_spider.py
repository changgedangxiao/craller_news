#coding=utf-8
import requests
from bs4 import BeautifulSoup
url="https://news.yahoo.com/least-three-police-officers-shot-houston-000758232.html"
resp=requests.get(url)
content=resp.content
soup=BeautifulSoup(content,"lxml")
# print soup.prettify()
title=soup.find("h1").string
print title
source=soup.find("span",attrs={"class":"provider-link"}).find("a").string
# .find("a",attrs={"class":"Fz(13px) C($c-fuji-grey-l)"}).string
print source
#     pass
time=soup.find("time",attrs={"itemprop":"datePublished"}).string
print time
content_list=soup.find_all("p",attrs={"type":"text"})
snippet=content_list[0].string
print snippet
content_str=""
for i in content_list:
    content_str+=i.string+"\n"
print content_str