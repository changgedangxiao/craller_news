# coding=utf-8


from craller_news.Common import code_conversion
from bs4 import BeautifulSoup
import re

from craller_news.mysql_jh import DBConn


html_path="../html/news.google/news.google.html"
soup=BeautifulSoup(open(html_path),features="lxml")
#新闻标题
news_title=soup.find(name="h1").string
#编码转换
news_title=code_conversion(news_title)
print "title:",news_title
#原标题
news_otitle=soup.find(name="p",attrs={"class":"otitle"}).string
news_otitle=code_conversion(news_otitle)
print news_otitle
#新闻来源和作者
author_source=soup.find(name="a",attrs={"id":"ne_article_source"})
news_author=author_source.string
news_author=code_conversion(news_author)
print"author:",news_author

news_source1=re.search(r'href="(.*?)"',code_conversion(author_source))
news_source=news_source1.group(1)
print "news_source:",news_source

# 提取新闻图片链接
img_list=soup.find_all(name="img")
img_source_list=[]
for img_source in img_list:
    img_source=code_conversion(img_source)
    img_source1=re.search(r'src="(.*?)"',img_source)
    img_source= img_source1.group(1)
    print img_source
    #过滤无效图片
    if img_source:
        if  not img_source.startswith("http") or img_source.endswith("jpg") or img_source.endswith("png"):
            pass
        else:
            img_source_list.append(img_source)
img_source_list=code_conversion(str(img_source_list))
print img_source_list
news_list=soup.find_all(name="p")
news_str=""
for i in news_list:
    news_str+=code_conversion(i.string)

#去除内容为None的段落
news_content=re.sub(r"None","",news_str)

print news_content

print type(news_title)
print type(news_otitle)
print type(news_author)
print type(news_source)
print type(news_content)
print type(img_source_list)

db_host = "127.0.0.1"
db_user = "root"
db_passwd = "Tianhu201"
db_name = "news"

db_conn = DBConn(db_host, db_user, db_passwd, db_name)
#title,NewsSnippet,parsedText,Source,Url,entity_list,Venue,imageLink,test3,NERTaggedText,test5
sql="""insert into NewsStories (title, NewsSnippet, parsedText, Source, Url, entity_list, Venue, imageLink,TimeStamp,NERTaggedText,entity_count) 
        values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")""" \
                %(news_title,news_content,news_otitle,news_author,news_source,"a","a",img_source_list,"a","a","a")

db_conn.insert_data(sql)