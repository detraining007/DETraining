#Fibonacci series
n=int(input("Enter the number of terms in series: "))
f=0
s=1
r=0
print(f, end=" ")
print(s, end=" ")
for i in range(n+1):
    r=f+s
    f=s
    s=r
    print(r,end=" ")
    
