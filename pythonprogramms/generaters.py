def generateItem(n):
    for i in range(n):
        yield i

if __name__=="__main__":
    n=int(input("Enter n value:"))
    for i in generateItem(n):
            print(i)
