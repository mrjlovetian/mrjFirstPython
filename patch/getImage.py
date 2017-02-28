import urllib.request
from bs4 import BeautifulSoup

url = input("please input url\n")

headers = {'headers':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'}

req = urllib.request(url, headers=headers)

html = req.urlopen(req)


# soup = BeautifulSoup(html)

print (html)