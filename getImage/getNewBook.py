# -*- coding:utf-8 -*-
import sys
import urllib, urllib2
from bs4 import BeautifulSoup


	# info = li.find_all('div')[1].find_all('div')
	# if info:
	#  	print info 


def getAllForeignBooks(url):
	new_book_url = url

	headers = {'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
	request = urllib2.Request(new_book_url, headers=headers)
	response = urllib2.urlopen(request).read()

	result = BeautifulSoup(response).find_all('li', class_='subject-item')
	for li in result:
		book_url = li.find_all('div')[0].find('a')['href']
		book_img = li.find_all('div')[0].find('img')['src']
		book_name = li.find_all('div')[1].find('h2').find('a')['title']
		book_author = li.find_all('div')[1].find('div', class_='pub')
		book_evalute = li.find_all('div')[1].find('div', class_='star clearfix')
		book_info = li.find_all('div')[1].find('p')
		book_price = li.find_all('div')[1].find('div', class_='cart-actions')

	# print (book_url, book_img, book_name, book_author, book_evalute, book_info, book_price)
	print ('我是小红君')
	print('地址:%s' %book_url)
	print('图片:%s' %book_img)
	print( book_name)
	print( book_author.text)
	print( book_evalute.find('span', class_='rating_nums').text)
	print( book_evalute.find('span', class_='pl').text)
	print(book_info.text)
	print('价格:%s' %book_price)

	print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

index = 0
while index < 200:
	getAllForeignBooks('https://book.douban.com/tag/%%E5%%A4%%96%%E5%%9B%%BD%%E6%%96%%87%%E5%%AD%%A6?start=%s&type=T'%index)
	print index
	index += 20


# print('result', response)