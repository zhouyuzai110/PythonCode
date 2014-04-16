# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math 
number = 3
list_sum = []
while number < 2000000:
	list_prime = []
	sqrtNum = math.sqrt(number+1)
	i = 2
	while i < sqrtNum:
	 	if number % i == 0 :
			list_prime.append(1)
		else:
			list_prime.append(2)
		i += 1 		

 	if list_prime.count(1) == 0:
 		list_sum.append(number)
 		print number
 	number += 2  #zhi suan jishu jisuanliang jianshao yiban
total_sum = sum(list_sum) + 2
print total_sum