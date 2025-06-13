def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2

if __name__=="__main__":
        n1=int(input("Enter n1:"))
        n2=int(input("Enter n2:"))
        c=int(input("Enter your choice:"))
        while(c):
            if c==1:
                print(add(n1,n2))
                break
            elif c==2:
                print(mul(n1,n2))
                break
            elif c==3:
                print(sub(n1,n2))
                break
            elif c==4:
                print(div(n1,n2))
            break
        else:
            print("")
            c=input("Enter correct choice")
           


            


            
