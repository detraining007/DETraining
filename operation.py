class operation(object):
    def __init__(self):
        self.x=10
    # def __add__(self,x):
    #     return self.x
if __name__=="__main__":
    obj1=operation()
    obj2=operation()
    sum=obj1+obj2
    print(sum)
