# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

# zhu yi kong lie biao de din yi weizhi ,yaozai xun huan ti zhi wai
xunhuan = True
a = 2520
while xunhuan:
	L = []
	for i in range(1,21):
		if a % i == 0:
			L.append(0)
		elif a % i != 0:
			L.append(1)
	lsum = sum(L)


	if lsum == 0:
		print a
		# xunhuan = False
		break
	else:
		a += 10 # yi zi you 10 suoyi yi ding neng bei 10 zheng chu
	
# Problem - 5

# Smallest multiple

# def smallest_multiple(limit):
# 	'''Finds the smallest positive number that
# 	is evenly divisible by all of the numbers 
#         from 1 to limit'''
# 	number = 2530
# 	i = 3
# 	while i <= limit:
# 		if number % i == 0:
# 			i += 1
# 		else:
# 			i = 3
# 			number += 10
# 	return number

# print smallest_multiple(20)
