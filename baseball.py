#-*- coding: utf-8 -*-
import random

while True:
	a = raw_input("야구 시작? ㅇㅇ 아니면 ㄴㄴ로 대답: ")
	if a=="ㅇㅇ":
		print "시작!"

#컴퓨터가 숫자를 돌리게 합니다.

		numbers = range(1,10)
		random.shuffle(numbers)
		num = numbers[0:4]
		print num

#사용자가 숫자를 입력하는 코드
		user = []
		while True:
			Input = raw_input("숫자 4개 입력:")
			if len(Input) !=4:
				print "4개만 치라고요"
			else:
				user.append(int(Input[0]))
				user.append(int(Input[1]))
				user.append(int(Input[2]))
				user.append(int(Input[3]))
			print user
			break

#컴퓨터랑 사용자 비교하는 코드: 스트라이크

		if num[0] == user[0]:
			r






				

		break

	elif a=="ㄴㄴ":
		print "ok bye~"
	else:
		print "ㅇㅇ/ㄴㄴ로."





		# if num[0] == 
# 	com.append(num)

# print com


# # print dir(random)