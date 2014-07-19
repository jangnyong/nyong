#-*- coding: utf-8 -*-

#알파벳으로만 or 알파벳/숫자로만
'''
s.isalnum()
s.isalpha()
s.strip()
s.strip().isalpha()
s.strip().isalnum()

#dictionary
d.copy()
d.get(key, default=None)
d.has_key(key) #키값에 지정한 값이 있으면 True, 아니면 False
d.items()
d.values()
d.keys()
d.update({'c':'d'})
d.clear()
'''

f=file('text.txt', 'r')

for line in f:
	print line,
	
f.close()

with file('text.txt', 'r') as text:
#text = file('text.txt', 'r')
	text.write("it was interesting")
	text.close()

#dictionary = {"a":1, "b":2}
