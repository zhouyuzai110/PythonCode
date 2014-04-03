while True:
	Sum = int(raw_input("Your Number : "))
	N = 0
	if Sum < 6 or Sum > 30:
		print "Your Number is out range!"
		continue
	else:
		for a in range(1,12):
			for b in range(1,12):
				for c in range(1,12):
					Total = a + b + c
					if Total == Sum:
						if a != b  and b != c and a != c:
							N += 1
							print N,a,b,c
	break						