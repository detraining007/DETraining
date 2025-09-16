def factorial(val1):
    result = 1
    for start in range(1,val1+1):
        result = result * start
    return result

def combination(val1,val2):
    return factorial(val1)/(factorial(val2)*factorial(val1-val2))




Lines = int(input("Please enter the no of rows u want in the pattern: "))
for val1 in range(Lines):
    print(" "*(Lines-val1),end="")
    for val2 in range(val1+1):
        print(int(combination(val1,val2)),end=" ")
    print()


