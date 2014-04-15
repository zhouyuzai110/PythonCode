# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2 digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 100
b = 100
ll = []
for a in range(100,1000):
	for b in range(100,1000):
		c = a * b 
		c1 = str(c)
		c2 = int(c1[::-1])
		if c == c2:
			ll.append(c)

ll.sort()
print ll			
			
		