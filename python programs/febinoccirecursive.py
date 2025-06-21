def fibinocci_recursive(n):
    if n<=1:
        return n
    else:
        return fibinocci_recursive(n-1)+fibinocci_recursive(n-2)
items=int(input("enter the number of items : "))
print("fionacci series")
for i in range (items):
    print(fibinocci_recursive(i))
