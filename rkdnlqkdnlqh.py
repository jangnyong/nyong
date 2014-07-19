#-*- coding: utf-8 -*-
import random

#묵찌빠부터 ㅇㅇ/ㄴㄴ까지를 한 while문 안에 넣어서 한 과정으로
#작은 구조를 짜고 나면 이거를 큰 구조로 바꿔서 틀을 바꾸는 게 어려웠음.
#def, class 쓸 생각보다는 좀 기본적인 거를 응용해보기.

while 1:
#묵찌빠 중에 뭘로 할지 치기
	while True:
		a = raw_input('묵찌빠?:')
		if a == '묵' or a == '찌' or a =='빠':
			print '니꺼: '+a
			break
		else: 
			print '묵찌빠로 쳐야함'

	#컴터가 출력해줄 거 섞기
	items = ['묵', '찌', '빠']
	random.shuffle(items)
	print '컴터꺼: '+items[1] #섞였으니까 몇 번째든 출력만 하면 됨

	#니꺼랑 컴터꺼랑 비교하기

	if items[1] == a:
		print '비김'

	elif items[1]!=a:
		if items[1] == '빠' and a=='묵':
			print '니가 짐'
		elif items[1] == '빠' and a=='찌':
			print '니가 이김'
		elif items[1] == '찌' and a=='빠':
			print '니가 짐'
		elif items[1] == '찌' and a=='묵':
			print '니가 이김'
		elif items[1] == '묵' and a=='찌':
			print '니가 짐'
		elif items[1] == '묵' and a=='빠':
			print '니가 이김'

	while True:
		b = raw_input('한번더???????????? ㅇㅇ 또는 ㄴㄴ로 대답하시오: ')
		if b == 'ㅇㅇ' or b == 'ㄴㄴ':
			print b
			break
		else:
			print 'ㅇㅇ이랑 ㄴㄴ이 어렵니'

	if b=='ㄴㄴ':
		print 'ok bye~'
		break
