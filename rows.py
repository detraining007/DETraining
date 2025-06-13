num=int(input("enter the number of rows"))

for i in range(1,num+1):
    print( (num-i)* " ",end="")
    print(i*"* ")
        
for i in range(num,0,-1):
    print((num-i)*" ",end="")
    print(i*"* ")

