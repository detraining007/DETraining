def armstrong(number):
    sum = 0
    power =len(str(number))

    while number > 0:
        rem = int(number%10)
        sum += rem**power
        number = number/10
    return  sum

number = int(input("Enter number"))
num = number
sum = armstrong(number)
# print(type(sum))
# print(type(num))
if (sum==num):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")