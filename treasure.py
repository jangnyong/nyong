#-*- coding: utf-8 -*-

f=open('treasure_map.txt', 'r')

for line in f:
	number = []
	for i in line:
		if i.isdigit()==True:
			number.append(i)
			''.join(number)
	print line[int(''.join(number))]

f.close()

#줄에서 숫자를 찾아서 그 번째에 있는 글자 찾기

f=open('treasure_map.txt', 'r')
for line in f:
	char = []
	for i in line:
		if !@#$%
		