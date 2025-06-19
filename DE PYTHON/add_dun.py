class op():
    def __init__(self):
        self.x=eval(input("enter number: "))
        self.y=eval(input("enter number: "))
    
    def __add__(self,x):
        return self.x+self.y
    
if __name__=='__main__':
    b1=op()
    b2=op()
    print(b1+b2)