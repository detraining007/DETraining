
def printPattern1(n):
    for i in range(1,n+1):
        s = n-i
        for j in range(s):
            print(' ',end=' ')
        p = i
        for j in range(p):
            print(' * ',end=' ')
        print()


if(__name__ == '__main__'):
    printPattern1(5)
