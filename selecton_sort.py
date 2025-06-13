n=int(input("enter length of list: "))
l=[]
for i in range(n):
    temp=int(input())
    l.append(temp)
print(l)
for i in range(n):
    min_ind=i
    for j in range(i+1,n):
        if l[j]<l[min_ind]:
            min_ind=l[j]
    l[i],l[min_ind]=l[min_ind],l[i]
print(l)
