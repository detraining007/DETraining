def list(n):
    for i in range(n):
        yield i  

if __name__ == "__main__":
    n = int(input("Enter a number: "))  
    for i in list(n):
        print(i)

    