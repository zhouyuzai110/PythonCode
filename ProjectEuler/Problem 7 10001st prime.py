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
	