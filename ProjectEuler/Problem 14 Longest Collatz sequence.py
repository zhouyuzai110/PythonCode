# The following iterative sequence is defined for the set of positive integers:

# n - n/2 (n is even)
# n - 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import datetime
start_time = datetime.datetime.now()

def CollatzProblem(number):
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    return count 

chain = []
i = 1
while i <= 1000000:
    chain.append(CollatzProblem(i))
    i += 1
max_start = max(chain)
max_start_index = chain.index(max_start)
print max_start_index, max_start 

end_time = datetime.datetime.now()
print end_time - start_time