# def bijiao(x):
# 	if x >10:
# 		return "dale"
# 	else:
# 		return "xiaole"
# bijiao(1)
# bijiao(11)

year = int(raw_input("your year : "))
if year % 400 == 0:
	print "ok!"
elif year % 4 == 0 and year % 100 != 0:
	print "ok!"
else:
	print "not!"