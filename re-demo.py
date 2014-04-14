import re
htmlfile = open("xx.htm","r").readlines()
outfile = open("out.txt","a")
# tanlan moshi jia ? bian cheng fei tanlan moshi
restr = re.compile("http.*?jpg")
for line in htmlfile:
	mingzhong = restr.search(line)
	if mingzhong and len(mingzhong.group()) < 120:
		outfile.writelines(mingzhong.group())
		outfile.writelines("\n")	
outfile.close()

