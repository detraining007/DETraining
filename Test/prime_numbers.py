def prime(n):
    for val in range(2,n):
        count = 0
        for val2 in range(2,n):
            if val%val2==0:
                count+=1
        if count==1:
            print(val)

    
         

if __name__ == "__main__":
    n=int(input("num: "))
    prime(n)
    