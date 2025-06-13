"""
n=[1,2,3,4,5,6,7,8,9,10]  
even_numbers=list(filter(lambda x:x%2==0,n))
print("even number: ",even_numbers)
"""

"""
from functools import reduce
n=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=reduce(lambda x,y:x+y,n)
print("odd number :",odd_numbers)
"""


sqr_lst=[1,2,3,4,5,6,7,8,9,10]
sqr_lst=list(map(lambda x:x*x,sqr_lst))
print(sqr_lst)
