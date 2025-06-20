<<<<<<< HEAD
n=int(input("enter the number of things: "))
chuncks=int(input("enter the number of bags: "))
c=[]
x=n//chuncks
r=n%chuncks
for i in range(chuncks):
    c.append(x)
index=0
for i in range(1,r+1):
    c[index]+=1
    index+=1
=======
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
>>>>>>> 95904fb3354e403a37a876779019fbdd2e0d26f6
print(f"Things can be divided in chunck as {c}")