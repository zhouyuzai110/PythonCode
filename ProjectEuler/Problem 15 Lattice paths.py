# Starting in the top left corner of a 2*2 grid, and only being able to 
# move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20*20 grid?

import datetime
start_time = datetime.datetime.now()


choose(4,2)
choose(40,20)
		
# This grid problem can be solved using finite mathematics. In a rectangular grid
# the amount of routes can be calculated as the combination of: C(w+h, h) or C(w+h, w).

# A 2x2 grid yields: C(2+2, 2) = 6

# In a 20x20 grid the number of routes is therefore: C(20+20, 20) = 137846528820















end_time = datetime.datetime.now()
print end_time - start_time