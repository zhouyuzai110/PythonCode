# Problem 18 Maximum path sum I.py

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# # NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, 
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, 
# and requires a clever method! ;o)

import datetime
start_time = datetime.datetime.now()

line1 = [75]
line2 = [95,64]
line3 = [17,47,82]
line4 = [18,35,87,10]
line5 = [20,04,82,47,65]
line6 = [19,01,23,75,03,34]
line7 = [88,02,77,73,07,63,67]
line8 = [99,65,04,28,06,16,70,92]
line9 = [41,41,26,56,83,40,80,70,33]
line10 = [41,48,72,33,47,32,37,16,94,29]
line11 = [53,71,44,65,25,43,91,52,97,51,14]
line12 = [70,11,33,28,77,73,17,78,39,68,17,57]
line13 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
line14 = [63,66,04,68,89,53,67,30,73,16,69,87,40,31]
line15 = [04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15]

def grid(x,y):
    list_x = lines[x-1]
    return list_x[y-1]   

start_number = grid(1,1)
i = 1
for line_order in range(2,16):
    print line_order,grid(line_order,i) ,grid(line_order,i + 1),
    if grid(line_order,i) < grid(line_order,(i + 1)):
        start_number += grid(line_order,(i + 1))
        i += 1
    else:
        start_number += grid(line_order,i)
        
    print grid(line_order,i) < grid(line_order,i + 1),i,start_number
    print "-------------------------"
print start_number


end_time = datetime.datetime.now()
print end_time - start_time





# # ln for lines, x for elements in a line

# with open("projecteuler_018_input.txt") as f:
#    triangle = [[int(x) for x in ln.split()] for ln in f]

# for ln in range(len(triangle)-2,-1,-1):
#     for x in range(len(triangle[ln])):
#         triangle[ln][x] = triangle[ln][x] + max(triangle[ln+1][x], triangle[ln+1][x+1])

# print(triangle[0][0])







# rows = []
# f = open('tring.txt', 'r')
# for line in f:
#     rows.append([int(x) for x in line.split()])

# for i in reversed(xrange(1, len(rows))):
#     for j in range(len(rows[i-1])):
#         x = rows[i][j]
#         y = rows[i][j+1]
#         z = rows[i-1][j]
#         if x > y:
#             rows[i-1][j] = x + z
#         else:
#             rows[i-1][j] = y + z
# print rows[0]





# Solution in Python. What I did was work from top to bottom.
# Python


# data = open('Problem 18.txt', 'r').read()
# data = [[int(y) for y in x.split(' ')] for x in data.split('\n')]
# sum = []
# temp = []
# for row in data:
#     if len(sum) == 0:
#         sum = row
#     elif len(sum) == 1:
#         temp = [sum[0]+index for index in row]
#         sum = temp[:]
#         temp = []
#     else:
#         for indiv in row:
#             if row.index(indiv) == 0:
#                 temp.append(indiv + sum[0])
#             elif row.index(indiv) == len(row) - 1:
#                 temp.append(indiv + sum[-1])
#                 sum = temp[:]
#                 temp = []
#             else:
#                 temp.append(indiv + max(sum[row.index(indiv)-1],sum[row.index(indiv)]))
# sum = temp[:]
# print max(sum)