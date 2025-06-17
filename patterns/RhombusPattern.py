number = int(input("Enter a number"))

for i in range(number):
    print(" "* (number-i),end="")
    for j in range(i+1):
      print("*",end=" ")
    print()
for i in range(number-1,0,-1):
    print(" " *(number-i+1),end="")
    for j in range(i):
        print("*",end=" ")
    print()

