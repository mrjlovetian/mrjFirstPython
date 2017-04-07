# -*- coding:utf-8 -*-
import urllib2, urllib, re
from bs4 import BeautifulSoup

doubanUrl = 'https://book.douban.com/'
headers = {'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
request = urllib2.Request(doubanUrl, headers=headers)
response = urllib2.urlopen(request).read()

result = BeautifulSoup(response)


resultHtml = result.find_all('ul', class_='list-col list-col5 list-express slide-item')
resultHtml1 = result.find_all('ul', class_='list-col list-col2 list-summary s')
resultHtml2 = result.find_all('ul', class_='list-col list-col5')

def getReult(html, att, name):
	if html:
		li_result = html[0].find_all('li')
		for li in li_result:
			li_div_list = li.find_all('div')
			if li_div_list:
				model = li_div_list[0]
				info = li_div_list[1]
				title = model.find(att)[name]
				image = model.find('img')['src']
				author = model
				print(title)
				print(image)
				# print(info.find(class_='price'))
				# print(info.find(class_='author'))

getReult(resultHtml, 'img', 'alt')
getReult(resultHtml1, 'img', 'alt')
getReult(resultHtml2, 'img', 'alt')






