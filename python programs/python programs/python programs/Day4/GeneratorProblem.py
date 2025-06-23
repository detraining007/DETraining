def generate(n):
    for i in range(n):
        yield i

if __name__ == "__main__":

    g = generate(int(input("Enter number")))

    for i in g:
       print(i)