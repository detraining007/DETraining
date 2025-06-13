def genarate(n):
    i=0
    while i<=n:
        yield i
        i+=2
obj=genarate(20)
for i in obj:
    print(i)
