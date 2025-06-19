def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def exit():
    return "exit"

if __name__=="__main__":
    while True:
        n1=int(input("Enter n1:"))
        n2=int(input("Enter n2:"))
        print("1.Add","\n 2.mul","\n 3.sub","\n 4.div","\n 5.exit")
        c=int(input("Enter your choice:"))
        if c==1:
            print(add(n1,n2))
            
        elif c==2:
            print(mul(n1,n2))
            
        elif c==3:
            print(sub(n1,n2))
            
        elif c==4:
            print(div(n1,n2))
            
        elif c==5:
            print(exit())
            break
        else:
            print("Invalid try again!")
                
           