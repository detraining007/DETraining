r=int(input("enter the number of rows"))
c=int(input("enter the numnber of columns"))
m=[]
for i in range(0,r):
    temp=[]
    for j in range(0,c):
        temp.append(int(input("enter element:")))
    m.append(temp)
#2nd matrix
print("2nd array before sorting:")
for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print("\n")
#converting matrix in linear list
linear_m=[]
for i in range(0,r):
    for j in range(0,c):
        linear_m.append(m[i][j])
#for sorting the linear matrix        
for i in range(0,r*c-1):
    for j in range(0,r*c-i-1):
        if linear_m[j]>linear_m[j+1]:
            linear_m[j],linear_m[j+1]=linear_m[j+1],linear_m[j]
m=[linear_m[i:i+c] for i in range(0,r*c,c)]
#2n array after sorting
print("2nd array after sorting:")
for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print("\n")