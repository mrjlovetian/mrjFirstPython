from bs4 import BeautifulSoup

from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:
	print(name.get_text())