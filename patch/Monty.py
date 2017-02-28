# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen

pymysql.install_as_MySQLdb()

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', 
	passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('use wikipedia')

def inserPageIfNotExists(url):
	cur.execute('select *from pages where url = %s', (url))
	if cur.rowcount == 0:
		cur.execute('insert into pages (url) values (%s)', (url))
		conn.commit()
		return cur.lastrowid
	else:
		return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
	print('select *from links where fromPageId = %s and toPageId = %s', (int(fromPageId), int(toPageId)))
	cur.execute('select *from links where fromPageId = %s and toPageId = %s', (int(fromPageId), int(toPageId)))
	if cur.rowcount == 0:
		cur.execute('insert into links (fromPageId, toPageId) Values (%s, %s)', (int(fromPageId), int(toPageId)))
	conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
	global pages
	if recursionLevel > 4:
		return
	pageId = inserPageIfNotExists(pageUrl)
	html = urlopen('http://en.wikipedia.org'+pageUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
		insertLink(pageId, inserPageIfNotExists(link.attrs['href']))
		if link.attrs['href'] not in pages:
			# 遇到一个新页面，加入集合并搜索里面的词条链接
			newPage = link.attrs['href']
			pages.add(newPage)
			getLinks(newPage, recursionLevel+1)
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()




















