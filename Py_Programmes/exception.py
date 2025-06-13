"""
SI = float(input("enter SI: "))
T = float(input("enter T: "))
R = float(input("enter R: "))
if T>10:
    print("Time cannot be greater than 10!")
try:
    P=SI*100/T*R

    print(P)
except Exception as error:
    print(error)
finally:
    print("always")
   """
"""
#for even
List=[i for i in [1, 3, 4, 5, 6, 7, 8] if i%2==0]
print(List)
"""
"""
#for odd
List=[i for i in [1, 3, 4, 5, 6, 7, 8] if i%2!=0]
print(List)
"""
"""
lst=[i+10 for i in [1,3,4,5,6,7] if i%2==0]
print(lst)
"""
"""
lst = [(n1+n2) for n1 in range(1,10) for n2 in range(11,20)]
print(lst)
"""
"""
lst = [(n1+n2) for n1 in range(1,10) for n2 in range(11,20)]
print(lst)
"""

"""
lst = [1,2,3,4,5,6,7,8]
even_numbers = list(filter(lambda x: x%2==0, lst))
print(even_numbers)
"""

lst = [1,2,3,4,5,6,7,8,9]
odd_numbers = list(filter(lambda x: x%2!=0, lst))
print(odd_numbers)

