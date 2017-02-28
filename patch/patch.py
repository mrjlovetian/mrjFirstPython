# -*- coding:utf-8 -*-
import re
import string
import sys
import os
import urllib

# 获得url
url = raw_input('please input url\n')

print(url)

# 抓取网页内容
htmlContent = urllib.urlopen(url).read()

# 提取网页链接
urllist = re.findall(r'src="(http.+?\.[jpg|png])"', htmlContent, re.I)


if not urllist:
	print('没有东西哇')
else:
	filePath = os.getcwd()+'/myImage'
	if os.path.exists(filePath) is False:
		os.mkdir(filePath)

	print('准备爬虫了')

	i = 1
	for imurl in urllist:
		temp = filePath+'/'+ str(i) + '.jpg'
		print(imurl)
		i += 1 
		urllib.urlretrieve(imurl, temp)
	print('图片下载完成')

