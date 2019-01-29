#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append("../../craller_news")
# url="https://news.yahoo.com/least-three-police-officers-shot-houston-000758232.html"
url="https://news.yahoo.com/kamala-harris-kicks-off-campaign-oakland-rally-defends-record-prosecutor-014352910.html"
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
    print i.string
    if i.string:
        content_str+=i.string+"\n"
print content_str

img_urls=soup.find_all("noscript")
print img_urls

for i in img_urls:
    i=unicode(i).encode("utf-8")
    ret=re.search(r'src="(.*)"',i)
    print ret.group(1)