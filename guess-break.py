# -*- coding:utf-8 -*- 
# break语句是用来 终止 循环语句的，即哪怕循环条件没有称为False或序列还没有被完全递归，也停止执行循环语句。
# 一个重要的注释是，如果你从for或while循环中 终止 ，任何对应的循环else块将不执行。
# 记住，break语句也可以在for循环中使用。
import random
guess = random.randint(1,100)
guess_time = 0
for i in range(1,10):
	while True:
		autoguess = random.randint(1,100)
		guess_time += 1
		if guess == autoguess:
			print "right guess is :",autoguess
			print "try guess_time is :",guess_time
			break