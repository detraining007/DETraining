class py (object):
    def __init__ (self):
        print("i am in py")
class python (py):
    def __init__(self):
        print("i am in python")
        super().__init__()
if __name__ == "__main__":
    obj = py()
    obj1 = python()
    obj1 = python()
    
        