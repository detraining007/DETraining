n=int(input("enter the number of things: "))
chuncks=int(input("enter the number of chuncks: "))
c=[]
x=n//chuncks
r=n%chuncks
for i in range(chuncks):
    c.append(x)
ind=0
for i in range(1,r+1):
    c[ind]+=1
    ind+=1
c1=[]
c1=list(filter(lambda x: x!=0,c ))

print(c1)
