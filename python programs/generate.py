def generateitem(n):
    new_list=[]
    for i in range(n):
        yield i
for i in generateitem(10):
    print(i)
    
