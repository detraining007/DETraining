
def printPattern3(n):
    for i in range(1,2*n): 
        s = n-i if i<=n else i-n
        for j in range(s):
            print(' ',end=' ')
        p = i if i<=n else 2*n-i
        for j in range(p):
            print(' * ',end=' ')
        print()


            
if(__name__ == '__main__'):
    printPattern3(5)
