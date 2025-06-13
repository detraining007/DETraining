def generation(n):
    for i in range(n):
        yield i
if __name__=="__main__":
    n=int(input("enetr number:"))
    for i in generation(n):
        print(i)