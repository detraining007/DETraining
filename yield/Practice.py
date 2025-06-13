def generator(n):
    for i in range(n):
        yield i

if __name__ =="__main__":
    for i in generator(5):
        print(i)



# def generator(n):
#     for i in range(n):
#         return i

# if __name__ =="__main__":
#     for i in generator(5):
#         print(i)



