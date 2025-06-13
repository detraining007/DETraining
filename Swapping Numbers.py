first = 3
second = 7
print("Numbers before swapping:")
print(f"first = {first}")
print(f"second = {second}")
temp = 0
temp = second
second = first
first = temp
print("Numbers after swapping:")
print(f"first = {first}")
print(f"second = {second}")


first_number = int(input("Please enter first number"))
second_number = int(input("please enter second number"))
print("Numbers before swap:")
print(f"first_number = {first_number}")
print(f"second_number = {second_number}")
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number
print("Numbers after swap:")
print(f"first_number = {first_number}")
print(f"second_number = {second_number}")


