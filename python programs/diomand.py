n=int(input("enter the number: "))
for i in range(n):
    for j in range(n-i):
        print('',end=' ')
    for k in range(i):
        print('*',end=' ')
    print(end='\n')


for i in range(n,0,-1):
    for j in range (n-i):
        print('',end=' ')
    for  k in range(i):
        print('*',end=' ')
    print(end='\n')
