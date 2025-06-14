CDn = 5

for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')

    C = 1

    for j in range(1, i+1):

        print(' ', C, sep='', end='')

        C = C * (i - j) // j
    print()


a=3
b=4
c=3*4+5
a+=10-2
print(a)

a=1
while a<10:
    print(a)
    a+=2

    x="datha"
print(x[1:-1])

#d4
a=1
b=5
c=3
print(a+b+c)

#d5
a="5"
a+="3"
t=int(a)+2
print(float(t))

#triangle
n=5
for i in range(1,n+1):
    for spaces in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
    #