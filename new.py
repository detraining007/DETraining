class myclass:
    def __new__(cls,age):
        print("creating a new")
        instance = super().__new__(cls)
        return instance
    def __init__(self, age):
        print("Inside __init__")
        self.age = age
obj = myclass(2)