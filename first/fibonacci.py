n1 = 0
n2 = 1
term = int(input("Enter the number: "))
if(term == 1):
    print("0")
if(term == 2):
    print("0, 1")
for i in range(term):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3