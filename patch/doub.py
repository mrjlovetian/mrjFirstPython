# -*- coding:utf-8 -*-
import urllib2, urllib
from bs4 import BeautifulSoup

url = 'http://www.dbmeinv.com/?pager_pffset=%1'

x = 0

# 伪装浏览器
def crawl(url):
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
	req = urllib2.Request(url, headers=headers)
	page = urllib2.urlopen(req, timeout=20)
	html = page.read()#获取源码

	soup = BeautifulSoup(html)
	my_girl = soup.find_all('img')# 找到img图片标签
	for girl in my_girl:
		link = girl.get('src')
		print('image', link)

		global x
		urllib.urlretrieve(link, 'imageFile/%s.jpg' % x)
		x += 1
# crawl(url)

for page in range(1, 5):
	page += 1
	url = 'http://www.dbmeinv.com/?pager_pffset=%s' % page
	crawl(url)




