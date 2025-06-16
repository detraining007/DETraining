import math
def printPattern1(n):
    for i in range(1,n+1):
        s = n-i
        for j in range(s):
            print(' ',end=' ')
        p = i
        for j in range(p):
            print(' * ',end=' ')
        print()


def printPattern2(n):
    for i in range(n):
        s = i
        for j in range(s):
            print(' ',end=' ')
        p = n-i
        for j in range(p):
            print(' * ',end=' ')
        print()

def printPattern3(n):
    for i in range(1,2*n): 
        s = n-i if i<=n else i-n
        for j in range(s):
            print(' ',end=' ')
        p = i if i<=n else 2*n-i
        for j in range(p):
            print(' * ',end=' ')
        print()

def printPattern4(n):
    for i in range(n):
        # for spaces
        for j in range(1,n+1-i):
            print(' ',end=' ')
        # for numbers
        for j in range(i+1):
            print(' ',math.comb(i,j),end=' ')
        print()
#

def printPattern5(n):
    for i in range(n):
        # inner loop for abcd
        for j in range(1,n+1-i):
            print(chr(64+j),end=' ')
        # for spaces
        for j in range(2*i-1):
            print(' ',end=' ')
        # for abcd in reverse order
        for j in range(n-i,0,-1):
            if i == 0 and j == n-i:
                continue
            print(chr(64+j),end=' ')
        print()


if(__name__ == "__main__"):
    
    printPattern4(6)


# A B C D E D C B A
# A B C D   D C B A
# A B C       C B A
# A B           B A
# A               A