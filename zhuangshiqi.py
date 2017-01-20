#-*- coding: UTF-8 -*- 
import time

def cost_time(func):
	def inner(*args, **kw):
		begin_time = time.time()
		print func.__name__ + ' start ' + str(begin_time)
		func(*args, **kw)
		end_time = time.time()
		print func.__name__ + ' end ' + str(end_time)
		cost = end_time - begin_time
		print "cost_time: %.4f" %cost
	return inner



		


@cost_time
def hello(num):
	for i in range(num):
		print 'hello world'


def digui(num):
	if num == 1:
		return 1
	return num + digui(num - 1)


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

hello(10)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.localtime()
print digui(100)
print fact(10)