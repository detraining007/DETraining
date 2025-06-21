class Base(object):
    def display(self):
        print("I am a base class")

class Derived1(Base):
    def display(self):
        print("I am Derived1")

class Derived2(Base):
    def display(self):
        print("I am Derived2")

def main():
    obj1 = Derived1()
    obj2 = Derived2()
    print(obj1.display())
    print(obj2.display())

if __name__ == "__main__":
    main()