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

g=open('treasure_map.txt', 'r')

char = []
for line2 in g:
	index = line2.find('!@#$%')
	if line2.find('!@#$%') !=-1:
		char.append(line2[index+5])


	'''
	if '!@#$%'+j in line2:
		# '!@#$%'+j == '!@#$%A'
		char.append(j)
		break
	'''
print char
g.close()

			
		