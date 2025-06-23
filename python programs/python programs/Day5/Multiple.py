class Father(object):
    def __init__(self):
        print("I am father")
class Child1(Father):
    def __init__(self):
        super().__init__()
        print("I am a child1")
class Child2(Father):
    def __init__(self):
        super().__init__()
        print("I am a child2")
class GrandChild(Child2,Child1):
    def __init__(self):
        super().__init__()
        print("I am a GrandChild")

obj = GrandChild()