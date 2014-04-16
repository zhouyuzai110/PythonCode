# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

list_100 = []
for i in range(1,101):
	list_100.append(i)
	sum100 = sum(list_100)
	total1 = sum100 ** 2

total2 = 0
for i in range(1,101):
	total2 += i ** 2

difference = total1 - total2
print difference