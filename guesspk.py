import random
def guess():
	a = []
	for i in range(3):
		a.append(int(random.randint(1,6)))
	return a 
com = 10
# play = 100
play = 10
while True:
	ComputerGuess = guess()
	PlayerGuess = guess()
	print ComputerGuess,PlayerGuess
	if sum(ComputerGuess) > sum(PlayerGuess):
		print "computer win~!"
		play -= 1
	else:
		print "player win~!"
		com -= 1
	# if com <= 0 or play <= 0:
	# 	print com,play
	# 	break
	if com <= 0 or play <= 0:
		if com > play:
			print com,play
			print "computer last win!"
			break
		else:
			print com,play
			print "player last win!"
			break

