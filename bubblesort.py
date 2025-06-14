n=int(input("enter length of list: "))
l=[]
for i in range(n):
    temp=int(input())
    l.append(temp)
print(l)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            
            l[j],l[j+1]=l[j+1],l[j]
print(l)