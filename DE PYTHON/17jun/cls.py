class de():
    def __init__(self):
        self.id=20
        self.num=23

    def getter(self):
        return f'id is {self.id}, marks are {self.num}'
    
    def paris(self):
        self.id = int(input("enter the number :"))
        self.num= int(input("enter the marks :" ))

if __name__=="__main__":
    n=int(input("enter the num 1 or 2 :"))
    boy=de()
    boy.paris()
    if n==1:
        print((boy.getter()))
    else:
        print(boy.id,boy.num)
