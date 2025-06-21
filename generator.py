
def generateItem(n):
    for i in range(n):
        yield i
if __name__=="__main__":
    generator=generateItem(int(input()))
    print(dir(generator))
    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())
    '''for i in generator:#i is iterating over object generator

def generateItem(n):
    for i in range(n):
        yield i
if __name__=="__main__":
    generator=generateItem(int(input()))
    print(dir(generator))
    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())
    '''for i in generator:#i is iterating over object generator
>>>>>>> 95904fb3354e403a37a876779019fbdd2e0d26f6
        print(i)'''