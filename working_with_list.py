# index = [i for i in range(10) if i % 2 == 0]
# print(index)

# name = input("what is your name? ")
# print("wow "+name.capitalize() +" you made it, its an input")

import math

# pi = 3.14
# print(math.sqrt(pi))

#finding the center of the list
"""to find the center of the list first the list should be an even or odd list,
   even list when divided has no remainder and so -1 should be applied on both
   side to get the center
   odd list when divided has a remainder and -1 on the left side should give 
   us the center"""
num = [2, 2, 4, 5, 4, 5]
# print(max(num))

#using len to find the center
# num=len(num)/2
# print(num)
# print(num[2], num[3])

#sorting and finding center
# num = sorted(num)
# print(num[2], num[3])

#using  slice(-2) and index(+2) to find the center of the list
# slicer = slice(2, -2)
# print(num[slicer])
#print(num[2:4])
#.............................................................................................

# for values in range(1,5+1):
#     print(values)
"""list comprehension"""
#print([values for values in range(1,5+1)])

# num=[values for values in range(1,100+1) if values % 2 == 0]
# dividers=[values for values in range(3,10+1)]
# if num/dividers == num-1:
#     print(num)

"""code not working yet"""
# num = []
# dividers = []
# for div in range(3,11):
#         dividers.append(div)
        
# for values in range(1, 100+1):
#     while (num/dividers == num-1):
#         num.append(values)
# print(num)

#excercises
# count=[num for num in range(1,21)]
# print(count)

milli=[value for value in range(1,9999999999999999+1)]
print(milli)
print(sum(milli))
print(max(milli))

mult =[mult for mult in range(3,30)]