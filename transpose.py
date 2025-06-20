r=int(input("enter the number of rows"))
c=int(input("enter the numnber of columns"))
m=[]
for i in range(0,r):
    temp=[]
    for j in range(0,c):
        temp.append(int(input("enter element:")))
    m.append(temp)
#2nd matrix
print("2nd array before transpose:")
for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print("\n")
b=[[0]*r for i in range(0,c)]
for i in range(0,r):
    for j in range(0,c):
        b[j][i]=m[i][j]
#2nd matrix after transponse

print("2nd array before after transpose:")
for i in range(0,c):
    for j in range(0,r):
        print(b[i][j],end=" ")
    print("\n")