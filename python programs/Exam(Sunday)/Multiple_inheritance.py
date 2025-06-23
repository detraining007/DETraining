class Parent(object):
   def land(self,number):
       self .number = number
       return f"{self.number} acres land"
class Child1(Parent):
    def car(self,car):
        self.car = car
        return f"{self.car} cars "
class Child2(Parent):
    def gold(self,gold):
        self.gold = gold
        return f"{self.gold} gold"
class Grand_Child(Child1,Child2):
    def house(self,house):
        self.house = house
        return f"{self.house} house"
obj = Grand_Child()
print(obj.car(2))
print(obj.gold(7))
print(obj.land(2))
print(obj.house(1))