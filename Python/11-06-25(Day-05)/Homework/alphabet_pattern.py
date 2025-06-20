#The print the pattern given below 
# A B C D E F E D C B A
# A B C D E   E D C B A
# A B C D       D C B A
# A B C           C B A
# A B               B A 
# A                   A

lst=['A', "B", "C", "D", "E", "F"]
# n is for no.of rows
n=6


#first loop for no. of rows
for row in range(n):
    #This loop is for printing forward
    for j in range(n-row):
        print(lst[j],end=" ")
    print("  " * (2*row-1),end="")

    #This loop is for printing reverse
    for j in range(n-row-1,-1,-1):
        if row==0 and j==n-row-1: #To skip the extra 'F'
            continue
        print(lst[j],end=" ")
    #To print in next line
    print()