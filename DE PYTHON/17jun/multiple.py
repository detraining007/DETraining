class home():
    def __init__(self):
        print("im in home go to the room of ")
    def go(self):
        print("")
class brother(home):
    def do(self):
        print("brothers room")
        
class sister(home):
    def come(self):
        print("sister room")
        print()
class common(home):
    def no(self):
        print("common hall")

if __name__=="__main__":
    dir=brother()
    dor=sister()
    dom=common()
    dir.do()
    dor.come()
    dom.no()
