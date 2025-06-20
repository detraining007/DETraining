class base_class():
    def __init__(self):
        print("Base class:")
class child(base_class):
    def __init__(self):
        print("child class")
if __name__=="__main__":
    obj1=child()
    print(obj1)