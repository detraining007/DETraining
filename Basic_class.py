class Arit_Methods():
    def __init__(self,value1,value2):
         self.value1 = value1
         self.value2 = value2
    def getter(self):
         return self.value1+self.value2
    def setter(self):
          self.value1 = 40
          self.value2 = 50
         

          
         
if __name__ == "__main__":
         obj1 = Arit_Methods(10,20)
         print(obj1.getter())
         obj1.setter()
         print(obj1.getter())
         
        