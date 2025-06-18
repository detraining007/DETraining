class Base():
    def __init__(self,value1,value2):
        self.value1 =value1
        self.value2 =value2
        print("This is Base class")
    def add(self):
        return self.value1 + self.value2
class Derived(Base):
    def __init__(self,value1,value2):
        super().__init__(value1,value2)
        print("This is Derived class")
    def add(self):
         print(f'{self.value1}-{self.value2}')
         return 
       
        
if __name__ == "__main__":
    obj1 = Derived(10,20)
    print(obj1.add())
    
    
