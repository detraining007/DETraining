try:
    x=int(input("enter a number"))
    m=10//x
    m=m+1
    print(m)
except  ZeroDivisionError:
    print("10 cannot be divided by zero")
    
finally:
    print("program is terminated")
