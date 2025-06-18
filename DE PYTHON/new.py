class de():
    def __init__(self):
        self.x=8
        print("im init")
    def __new__(cls):
        print("new")
        cls.nm=input()
        return super().__new__(cls)
if __name__=="__main__":
    boy=de()
    print(boy.x)
    print(type(boy))
    print(de.nm)
