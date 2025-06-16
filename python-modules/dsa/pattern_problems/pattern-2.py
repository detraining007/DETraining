def printPattern2(n):
    for i in range(n):
        s = i
        for j in range(s):
            print(' ',end=' ')
        p = n-i
        for j in range(p):
            print(' * ',end=' ')
        print()

if(__name__ == '__main__'):
    printPattern2(5)


