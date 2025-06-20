#To understand the working of init and new methods in classes(Both are initializers)

#Simple program
# class Test:
#     def __init__(self):
#         print("Im in init")

#     def __new__(cls):
#         print("Im in new method")
#         return super().__new__(cls)

# if __name__=="__main__":
#     test1=Test()
#     print(test1)

class add():
    
    def __init__(self):
        print("Im in init")
        self.x=3
        self.y=5

    def __new__(cls):
        print("Im in new")
        return super().__new__(cls)
        #return "SAI RAM "

    def getter(self):
        return self.z
    
    def setter(self):
        self.x=int(input("enter x value: "))
        self.y=int(input("Enter y value: "))
        self.z=self.x+self.y
    
if __name__=="__main__":
    test1=add()
    print(test1.x,test1.y)
    setter1=test1.setter()
    val=test1.getter()
    print(val)

