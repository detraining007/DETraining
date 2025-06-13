I=float(input("enter intrest:"))
T=float(input("enter time:"))
R=float(input("enter rate:"))
try:
    P=(I*100)/(T*R)
    print("Principle amount is:",P)
except Exception as error:
    error=print("T and R Cannot be Zero")
    raise



    








