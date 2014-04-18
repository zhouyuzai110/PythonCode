# Problem 17 Number letter counts.py

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use
#  of "and" when writing out numbers is in compliance with British usage.

# import re

# dig=['one','two','three','four','five','six','seven','eight','nine']
# dec=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# spc={10:'ten',11:'eleven',12:'twelve',13:'thirteen',15:'fifteen',18:'eighteen'}

# def num2text(n):
#   word = ''
#   if n == 1000:
#     return 'one thousand'

#   if n > 99:
#     word += dig[(n/100)-1]
#     word += ' hundred'
#     n = n % 100
#     if n > 0:
#       word += ' and '

#   if n >= 20:
#     word += dec[(n/10)-2]
#     if n % 10 > 0:
#       word += "-%s" % dig[(n%10)-1]
#   elif n in spc.keys():
#     word += spc[n]
#   elif n > 0:
#     word += dig[(n%10)-1]
#     if n / 10 > 0:
#       word += 'teen'

#   return word

# def count(nr):
#   return len(re.sub(r'[^a-z]', '', nr))

# total = 0
# for i in range(1,1001):
#   txt = num2text(i)
#   total += count(txt)
#   print "%s => %d => %d" % (txt, count(txt), total)

# print total







# from num2words import num2words
# Sum = 0
# for i in range(1,1001):
#     input = num2words(i)
#     output = ''.join( [c for c in input if c not in ' -' ] ) 
#     Sum += len(output)
# print Sum








# import time
 
# start = time.time()
 
# S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
# D = [0,3,6,6,5,5,5,7,6,6]
# H = 7
# T = 8
 
# total = 0
# for i in range(1,1000):
#     c = i % 10 # singles digit
#     b = ((i % 100) - c) / 10 # tens digit
#     a = ((i % 1000) - (b * 10) - c) / 100 # hundreds digit
 
#     if a != 0:
#         total += S[a] + H # "S[a] hundred
#         if b != 0 or c != 0: total += 3 # "and"
#     if b == 0 or b == 1: total += S[b * 10 + c]
#     else: total += D[b] + S[c]
 
# total += S[1] + T
# elapsed = time.time() - start
 
# print "%s found in %s seconds" % (total,elapsed)