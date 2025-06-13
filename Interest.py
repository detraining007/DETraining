def Interest():
    try:
        principal = int(input("Enter the principal amount: "))
        rate = int(input("Enter the annual interest rate (in %): "))
        time = int(input("Enter the time in years: "))

        interest = (principal * time * rate) / 100
        print("The interest is: ", interest)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    finally:
        print("Thank you for using the interest calculator.")

Interest()

