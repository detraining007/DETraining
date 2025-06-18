class datha():
     def __new__(op1):
        print("what is curry")
        return super().__new__(op1)
     def __new__(self3):
        print("vankaya pulusu")
        return super().__new__(self3)
     def __init__(self):
       self.a=100
       self.b=200
     def set(self,a1,b1):
       self.a=a1
       self.b=b1
     def getter(self):
        return self.a,self.b
if __name__=="__main__":
    obj=datha()
    print(obj.a)
    print(obj.b)
    obj.set(5,8)
    print(obj.getter())