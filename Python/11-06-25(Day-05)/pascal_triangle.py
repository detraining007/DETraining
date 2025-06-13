#To write a program to print pascals triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

#Factorial function
def factorial(n):
    fac=1
    for num in range(1,n+1):
        fac=fac*(num)
    return fac

#Definition of ncr function
def ncr_function(n,r):
    ans=(factorial(n)//((factorial(n-r))*factorial(r)))
    return ans

#Main fuction - function callings
rows=int(input("Enter the number of rows: "))
for num in range(rows):
    for spaces in range(rows-num):
        print(end=" ")
    for col in range(num+1):
        print(ncr_function(num,col),end=" ")
    print("\n")

    