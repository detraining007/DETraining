name = input("Enter a String")
name = name.lower()
j=len(name)-1
c=0
for i in range(j):
    if(name[i]!=name[j]):
        c=c+1
        break
    j-=1
if(c>0):
    print("not a plaindrome")
else:
    print("palindrome")

a=10
b=20
c=a+b
print(c)


