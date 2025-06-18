class Test(object):
   def __new__(cls,value1,value2):
       print("I am in class new")
       return super().__new__(cls)
   def __init__(self,value1,value2):
       self.value1 = value1
       self.value2 = value2
   def getter(self):
       return self.value1+self.value2
   def setter(self):
       self.value1 = 100
       self.value2 = 200
   
        
    
if __name__ == "__main__":
    obj1 = Test(10,20)
    obj1.setter()
    print(obj1.getter())