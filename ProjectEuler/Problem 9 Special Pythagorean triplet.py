# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1000):
	for b in range(1000):
		for c in range(1000):
			if a < b < c and a + b + c == 1000:
				if a ** 2 + b ** 2 == c ** 2:
					print a,b,c
					break


# #!/usr/bin/python

# def s_p_t(a,c):
#     return a*a+(1000-a-c)**2==c*c

# for a in range(1,334):    #3a<1000 so a<=333
#     for c in range(499,333,-1):    #3c>1000 so c>=334; a,b,c make a triangle, c<a+b ==> 2c<a+b+c=1000 ==>c<500
#         if s_p_t(a,c):
#             b=1000-a-c
#             print a*b*c    #cheat here: i'm told by the question that the answer is unique. If i didn't know it, just save the result and let the loops go to end.


# def f():
#     for hyp in xrange (334, 500):
#         finish = hyp - 1
#         start = 500 - hyp/2
#         for side in xrange(start, finish):
#             difference = (hyp**2 - side**2)**0.5
#             if difference == 1000 - side - hyp:
#                 return int(difference)* side * hyp            