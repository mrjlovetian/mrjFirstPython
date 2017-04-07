import urllib2, urllib
import re
from bs4 import BeautifulSoup

url = 'https://tieba.baidu.com/p/4989867216'

x = 1
def get_image_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req, timeout=2)
    html = page.read()
    images_list = BeautifulSoup(html).find_all('img')
    global x
    for image_url in images_list:

        girl_url = image_url.get('src')
        result = re.search('.jpg', girl_url)
        print (result, girl_url)
        if (girl_url.endswith('.jpg')):
        	urllib.urlretrieve(girl_url, 'imageFile/%s.jpg'%x)
        # elif (girl_url.endswith('.gif')):
        	# urllib.urlretrieve(girl_url, 'imageFile/%s.gif'%x)
        elif (girl_url.endswith('.png')):
        	urllib.urlretrieve(girl_url, 'imageFile/%s'%x)
        x += 1
        
get_image_url(url)
