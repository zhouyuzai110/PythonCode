# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiple(x):
	multiple_listx = []
	a = 0
	while a < 1000:
		if a % x == 0:
			multiple_listx.append(a)
		a += 1
	return multiple_listx

x3 = multiple(3)
x5 = multiple(5)
# zhu yi gong yue shu
total_x =  x3 + x5
total_x = list(set(total_x))
total_sum = sum(total_x)

print total_sum

# print sum([item for item in xrange(1,1001) if item%3 == 0 or item%5 == 0])



# Problem - 1

# Multiples of 3 and 5

# def multiples(limit):
# 	'''Finds the sum of all the multiples
# 	of 3 or 5 below limit'''
# 	i = 1
# 	sum_of_multiples = 0
# 	while i < limit:
# 		if (i % 3 == 0) or (i % 5 == 0):
# 			sum_of_multiples += i
# 		i += 1
# 	return sum_of_multiples

# print multiples(1000)


# result = 0
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         result = result + i
# print str(result)