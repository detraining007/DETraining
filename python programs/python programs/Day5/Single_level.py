class Calculation(object):
    def variables(self):
        self.x = 10
        self.y = 25
        self.z = 8
        return ( "calculation class called")

class Addition(Calculation):
     def addition(self):
         super().variables()
         sum= self.x + self.y +self.z
         return sum

obj = Addition()
print(obj.variables())
print(obj.addition())