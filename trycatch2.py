try:
    n=int(input("Enter the number: "))
    m=15//n
    m=m+1
    print(m)
except ZeroDivisionError:
    print("15 cannot be division by zero")
else:
    print("No error")
    print("end of the progarm")

