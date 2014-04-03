def guess():
	a = range(1,11)
	b = range(1,11)
	c = range(1,11)
	d = range(1,11)
	e = range(1,11)
	f = range(1,11)
	guess = int(raw_input("your number is : "))
	guess_time = result = prerssult = 0
	if guess >= 21 and guess <= 45:
		for a in range(1,11):
			for b in range(1,11):
				for c in range(1,11):
					for d in range(1,11):
						for e in range(1,11):
							for f in range(1,11):
								guess_time += 1
								he = a + b + c + d + e + f
								if he == guess:
									prerssult += 1
									if a < b < c < d < e < f:
										print a,b,c,d,e,f
										result += 1
		print result,"results!",
		print "done! try",guess_time, "times",prerssult, "sum iqute"
	else:
		print "out range"

for i in range(10):
	guess()
