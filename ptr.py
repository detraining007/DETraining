def Interest():
    try:
        p = int(input("Enter principal amount: "))
        t = int(input("Enter annual interest rate in(%): "))
        r = int(input("Enter time in years: "))
        if r > 10:
            raise Exception("years cannot be greater than 10")  
        interest = (p * t * r ) / 100
        print("The interest is: ", interest)

    finally:
        print("EXIT")

Interest()
              

