n=int(input("enter the number of things: "))
chunks=int(input("enter the number of chuncks: "))
c=[]
x=n//chunks
r=n%chunks
for i in range(chunks):
    c.append(x)
index=0
for i in range(1,r+1):
    c[index]+=1
    index+=1
print(f"Things can be divided in chunck as {c}")
