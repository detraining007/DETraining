def generateItem(n):
    for i in range(n):
        return i
    if __name__=="__main__":
        generator=generateItem(int(input()))
        print(generator)