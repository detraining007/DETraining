def generateItem(n):
    for i in range(n):
        yield i
if __name__=="__main__":
    generator=generateItem(int(input()))
    print(dir(generator))
    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())
    for i in generator:#i is iterating over object generator
        print(i)
