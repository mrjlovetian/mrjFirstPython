import urllib2,urllib 
from bs4 import BeautifulSoup

url = 'http://www.dbmeinv.com/?pager_pffset=%1'

x = 1

def getGirlImage(url):
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
	req = urllib2.Request(url, headers=headers)
	page = urllib2.urlopen(req)
	imageList = BeautifulSoup(page).find_all('img')

	global x
	for girl_url in imageList:
		print girl_url.get('src')
		urllib.urlretrieve(girl_url.get('src'), 'imageFile2/%s.jpg'%x)
		x += 1
getGirlImage(url)