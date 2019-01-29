#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import os
import time
def get_cates_url():
    root_url="https://news.google.com"
    req=None
    try:
        req=requests.get(root_url)
    except Exception as e:
        print "requests error:",e
    if not req:
        return
    content=req.content
    soup=BeautifulSoup(content,features="lxml")
    ret=re.search(r"//(.*).com",root_url).group(1)
    if not os.path.exists("../html/"+ret):
        os.mkdir("../html/"+ret)
        with  open("../html/"+ret+"/"+ret+".html","w") as f:
            f.write(soup.prettify().encode("utf-8"))

    #谷歌新闻类别
    news_cates=["U.S.","World","Business","Technology","Entertainment","Sports","Science","Health"]
    #获取新闻类别的url
    cates_url=[]
    for cate in news_cates:
        cate_url=soup.find("a",attrs={"aria-label":cate}).attrs.get("href",None)[1:]
        cates_url.append(root_url+cate_url)

    #新闻类别对应其url的字典
    news_cates_url=dict(zip(news_cates,cates_url))

    for cate in news_cates_url:
        url = news_cates_url[cate]
        req = None
        try:
            req = requests.get(url)
        except Exception as e:
            print "requests error", e

        if req:
            if not os.path.exists("../html/"+ret+"/"+ cate):
                os.mkdir("../html/"+ret+"/"+ cate)
            content = req.content
            soup = BeautifulSoup(content, features="lxml")
            with  open("../html/" +ret+"/"+ cate + "/" + cate + ".html", "w") as f:
                f.write(soup.prettify().encode("utf-8"))
        print cate+" finished"



if __name__ == '__main__':
    s_time = time.time()
    get_cates_url()
    e_time = time.time()
    cost_time = e_time - s_time
    print cost_time