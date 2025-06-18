class home():
    def __init__(self):
        print("im in home")
    def go(self):
        print("go room")

class room(home):
    def work(home):
        print("go to kicthen")

class kicthen(room):
    def cook(home):
        print("biryani ready")

if __name__=="__main__":
    time=kicthen()
    time.go()
    time.work()
    time.cook()

