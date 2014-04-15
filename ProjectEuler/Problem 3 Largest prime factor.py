# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


target_number = 600851475143
i = 2
while target_number % i != 0:
	i += 1
	if target_number % i == 0:
		print i
		target_number /= i
		continue

	if 	target_number == 1:
		break




