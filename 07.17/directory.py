# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import os
'''
f = open('%s.txt', % url'w')
list = range(1,2000)
for i in list:
    data = urllib.urlopen("http://www.huffingtonpost.kr/2014/07/16"+str(i)+'1414.html?utm_hp_ref=korea').read()
    bs = BeautifulSoup(data)
    sammies = bs.find_all("p")
    for s in sammies:
        f.write(s.text.encode('utf-8'))
    
f.close()
'''


data = urllib.urlopen("http://www.huffingtonpost.kr/2014/07/16/").read()
soup = BeautifulSoup(data)
bs = soup.select("h3 a")

for b in bs:
	file_name = b.text.replace("!", "").replace(":", "").replace("?","").replace("\"","") + ".txt"
	f=open(file_name, "w")
	data1 = urllib.urlopen(b['href'])
	soup1 = BeautifulSoup(data1)
	c = soup1.select("div#mainentrycontent p")
	for s in c:
		f.write(s.text.encode('utf-8'))
	f.close()
