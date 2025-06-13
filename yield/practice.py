def generator(n):
    for value in range(n):
        yield value
if __name__ == "__main__":
    output = generator(5)
    for i in generator(5):
        print(i)
