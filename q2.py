# multiple inhertiance
class animals:
    def lion(self, sleep):
        roar = self.sleep
        return self.sleep
class birds:
    def peacock(self, dance):
        dance = self.dance
        return self.dance
class humans(animals, birds):
    def maneesh(self, eat):
        eat = self.eat
        return self.eat
abc = humans()
print(abc)