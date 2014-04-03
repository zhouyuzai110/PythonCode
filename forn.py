a = ["one","two","three"]
b = ["xxx","yyy","zzz"]
c = ["if","for","while"]
for i in a:
	for j in b:
		for k in c:
			print i,j,k
else:
    print 'The for loop is over'
s = a + b
print s
print s[0:3] * 3
print "%s in %s" %(a,b)

