#coding=utf-8
from bs4 import BeautifulSoup
import re
from craller_news.mysql_jh import DBConn

def deal_html(html_path="../fetch_html/1.html"):

    soup=BeautifulSoup(open(html_path))
    news_title=soup.title.string
    news_author=soup.find(name="p",attrs={"class":"author-name"}).string
    news_source=soup.find()
    news_list=soup.find_all(name="span",attrs={"class":["bjh-p","source"]})
    news_str=""
    for i in news_list:
        str=unicode(i.string).encode("utf-8")
        news_str+=str

    #去除内容为None的段落
    news_content=re.sub(r"None","",news_str)
    return news_title,news_author,news_content


for i in deal_html():
    print i
db_host = "127.0.0.1"
db_user = "root"
db_passwd = "Tianhu201"
db_name = "news"

db_conn = DBConn(db_host, db_user, db_passwd, db_name)
db_conn.insert_data()
