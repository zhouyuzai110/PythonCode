import random
for i in range(100):
	times = 0
	loop = 0
	while times < 10000:
		a = random.randint(1, 11)
		b = random.randint(1, 11)
		c = random.randint(1, 11)
		d = random.randint(1, 11)
		e = random.randint(1, 11)
		loop += 1
		if a != b != c != d != e:
			times += 1
			# print a,b,c,d,e
	else:
		times = float(times)
		loop = float(loop)
		pp = times / loop
		print times,"times","porp is :", pp