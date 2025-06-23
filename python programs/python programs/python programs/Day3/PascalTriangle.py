num = int(input("Enter a number"))
# num = num-2

for i in range(num):
    a = 11 ** i
    digit_list = [int(digit) for digit in str(a)]
    space = num - i+1
    print(" " * space, end="")
    for j in range(len(digit_list)):
        print(digit_list[j],end=" ")
    print()