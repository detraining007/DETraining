def generateItem(n):
    New_List=[]
    for i in range(n):
        yield i                   

# for i in generateItem(10):
#         print(i)
New_List = list(generateItem(6))
print(New_List)