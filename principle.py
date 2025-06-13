


try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    # print("Can't divided by zero")
    raise Exception("Can't divided by zero")

finally:
    print("This is always executed")