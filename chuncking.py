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
print(f"Things can be divided in chunck as {c}")