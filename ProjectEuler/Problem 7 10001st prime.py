# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

order = 1
number = 2
while order < 10002:
	list_prime = []
	for i in range(1, (number + 1)/2+1):
	 	if number % i == 0 :
			list_prime.append(1)
		else:
			list_prime.append(2)
		 		

 	if list_prime.count(1) == 1:

 		order += 1

	number += 1
 		
	print number,order	
	


# import time, math

# #finding the 10001 th prime

# strtTime = time.time()

# #prime check
# def ifPrime(chckNum,primeList):
#     n = 0
#     isPrime = False
#     sqrtNum = math.sqrt(chckNum+1)
#     #using seive of Erat
#     while (primeList[n] < sqrtNum):
#         if chckNum % primeList[n] == 0:
#             return 
#         else:
#             isPrime = True
#         n += 1
#     if isPrime == True:
#         primeList.append(chckNum)
#     return

# primeList = [2,3]
# chckNum = 5
# while (len(primeList)<3):
#     ifPrime(chckNum,primeList)
#     chckNum += 2


# print time.time() -strtTime
# print primeList[-1]









# def nth_prime(n):
# 	prime_count = 0
# 	index = 2
# 	current_array_size = 1000000
# 	a = [0]*current_array_size

# 	while (index < current_array_size):
# 		if a[index] == 0:
# 			prime_count += 1
# 			a[index] = 1

# 			for k in xrange(current_array_size/index):
# 				a[k*index] = 1

# 		if prime_count == n:
# 			return index

# 		index += 1

# 	return "error: array not big enough"

# print nth_prime(10001)