# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import os
import codecs

data = urllib.urlopen("http://openapi.naver.com/search?key=763fe70a72ff29efbf3cb011d20e0e6f&query=%EC%A3%BC%EC%8B%9D&target=news&start=1&display=30").read()
soup = BeautifulSoup(data)
bs = soup.select("item")


count = 0


 
for b in bs:
	title = b.select("title")[0]
	link = b.select("originallink")[0]

	title = title.text.replace("!", "").replace("'","").replace(":", "").replace("?","").replace("\"","").replace("<b>","").replace("</b>","").replace("[","").replace("]","") + ".html"

	# print link.text


	if link.text != "":
		count = count + 1
		f= codecs.open(title, "w", "utf-8")
		data1 = urllib.urlopen(link.text)
		soup1 = BeautifulSoup(data1)
		c = soup1.select("html")[0]

		f.write(c.encode("ascii"))
		f.close()

	if count == 20:
		break		
