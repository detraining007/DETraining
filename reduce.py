#A program to understand reduce function in list comprehension
#The program is to print sum of all elements in the list

from functools import reduce
lst=[0,1,2,3,4,5,6,7,8,9,10]
sum= reduce(lambda x,y:x+y,lst)
print("Sum of all elements of the list is: "sum)