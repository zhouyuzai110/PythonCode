import os
KeyWord = "TRUE"
KeyWordx = "[1]"




def FileList():
	WorkDirFiles = os.listdir(os.getcwd())
	lists = []
	for FileNames in WorkDirFiles:
		if FileNames[6:10] == "Freq" or FileNames[7:11] == "Freq":
			lists.append(FileNames)
	return lists

for files in FileList():
	OutFileName = files + "-out.txt"
	PreFile = open(files,"r").readlines()
	for lines in PreFile:
		if KeyWord in lines:
			outlines = lines.replace("TRUE","").replace("     ","")
			outfile = open(OutFileName,"a")
			outfile.write(outlines)

DayFile = open("1-115-Freq.txt","r").readlines()
for linex in DayFile:
	if KeyWordx in linex:
		outlinex = linex.replace("[1]","").replace("\"","").replace(" ","")
		outfilex = open("Days.txt","a")
		outfilex.write(outlinex)