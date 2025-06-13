# try:
#     principal = float(input("Enter principal amount: "))
#     rate = float(input("Enter rate of interest (per annum): "))
#     time = float(input("Enter time (in years): "))

#     simple_interest = (principal * rate * time) / 0

#     print(simple_interest)
# except Exception as err:
#     # pass
#     # print("So the exception is ", err)
#     raise
# finally:

#     print("in an finnal stage")




try:
    # import adsdada
    a=10
    b=20
    print(a+b+c)
except Exception as err:
    print("so the exception is :", err)
    pass
finally:
    print("In finnal stage")
