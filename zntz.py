# Number = int(raw_input('zhui hao qi shu : '))
# Times = int(raw_input('qi shi bei shu : '))
# Yield = float(raw_input('ying li lv : '))
# JiangJin = int(raw_input('jiang jin : '))

Number = 78
Times = int(raw_input('Begin Times : '))
Yield = float(raw_input('Get precent : '))
JiangJin = 130

TotalCost = 0
QiCi = 0

FileName = "%s-%s-%s.txt" %(Times,Yield,Number)

for i in range(Number):
	NowCost = 2 * Times
	TotalCost = NowCost + TotalCost
	PayMe = Times * JiangJin - TotalCost
	MeGetPrecent = float(PayMe) / float(TotalCost)
	
	while MeGetPrecent < Yield:
		LoopTime = 1
		NowCost = 2 * LoopTime + NowCost
		TotalCost = TotalCost + 2 * LoopTime
		PayMe = (Times + LoopTime) * JiangJin - TotalCost
		MeGetPrecent = float(PayMe) / float(TotalCost)
		LoopTime += 1
		Times += (LoopTime - 1)	
	QiCi += 1
	print QiCi, Times, NowCost, TotalCost, PayMe, MeGetPrecent
	
	out = "%s %s %s %s %s %s" %(QiCi, Times, NowCost, TotalCost, PayMe, MeGetPrecent)
	f = open(FileName,"a")
	f.write(out)
	f.write("\n")
f.close()
