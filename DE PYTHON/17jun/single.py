class home():
    def __init__(self):
        self.x=9
        print("im in home")
    def go(self):
        print("go home")

class room(home):
    def __init__(self):
        print("im in room")

if __name__=="__main__":
    time=room()
    road=home()
    print(road.x)