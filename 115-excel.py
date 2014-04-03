import os
import xlrd
# outfile = open("out.txt","w+")
outfile = open("out.txt","a")
filelist = os.listdir(os.getcwd())
for name_book in filelist:
	if name_book[-1] == "s":
		wb = xlrd.open_workbook(name_book)
		name_sheet = wb.sheet_names()
		for sheetnames in name_sheet:
			table = wb.sheet_by_name(sheetnames)
			nrows = table.nrows
			for rownum in range(nrows):
				n5 = str(table.row_values(rownum))
				outfile.write(n5)
				outfile.write('\n')
				# print table.row_values(rownum)
outfile.close()
# 13122042	10	6	2	8	9 queshi yong li jin shuju buchong


list1 = open("out.txt","r").readlines()
orderfile = list(set(list1))
orderfile.sort()
for line in orderfile:
	line1 = line.replace("[","").replace("]","").replace(".0","")
	f = open('order.txt','a')
	f.writelines(line1)
f.close()