
n = int(input("Enter how many columns you want :"))
spaces = n
star = 1

for i in range(n):

    for j in range(spaces):
        print(" ",end="")
    spaces -= 1
    for k in range(star):
        print("*",end=" ")
    star +=1

    print("\n")