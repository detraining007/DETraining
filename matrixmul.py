
def mul(l1,l2):
    r1=len(l1)
    c1=len(l1[0])
    r2=len(l2)
    c2=len(l2[0])
    if c1!=r2:
        print("Invalid choice")
        return -1
    res=[[0]*c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j]+=l1[i][k]*l2[k][j]
    return res
r1=int(input("enter number of rows in l1: "))
c1=int(input("enter the number of columns in l1:"))
l1=[]
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    l1.append(row)
r2=int(input("enter number of rows in l2: "))
c2=int(input("enter the number of columns in l2:"))
l2=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    l2.append(row)
=======
def mul(l1,l2):
    r1=len(l1)
    c1=len(l1[0])
    r2=len(l2)
    c2=len(l2[0])
    if c1!=r2:
        print("Invalid choice")
        return -1
    res=[[0]*c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j]+=l1[i][k]*l2[k][j]
    return res
r1=int(input("enter number of rows in l1: "))
c1=int(input("enter the number of columns in l1:"))
l1=[]
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    l1.append(row)
r2=int(input("enter number of rows in l2: "))
c2=int(input("enter the number of columns in l2:"))
l2=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    l2.append(row)
>>>>>>> 95904fb3354e403a37a876779019fbdd2e0d26f6
print(mul(l1,l2))