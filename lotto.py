#-*- coding: utf-8 -*-
#1-45까지의 번호 중에 6개의 번호 뽑기
import random

num=range(1, 46)
random.shuffle(num)
print num[0:6]
