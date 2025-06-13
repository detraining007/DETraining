rows=6
for i in range(rows):
    for j in range(rows-i):
        print("*",end=" ")
    print()
    
for i in range(rows):
        for space in range(i):
           print(" ",end=" ")
        for j in range(rows-i):
           print("*",end=" ")
        
        print()
