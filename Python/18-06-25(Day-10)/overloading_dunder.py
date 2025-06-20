#To implement Overloading for __add__() function

class Test(object,x,y):
    def __init__(self):
         self.x=3
         self.y=6
        
        
    def __add__(self,x):
        self.z=self.x+self.y

        return self.z
    
if __name__=="__main__":
    test1=Test(10)
    test2=Test(9)
    # test3=Test()
    # test4=Test()
    print(test1+test2)
    
    

