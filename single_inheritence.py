class vechiles:
    def car(self):
        return "fortuner, thar, tata"

class bikes(vechiles):
    def method(self):
        return "bmw, royal enfield"

abc = bikes()
print(abc.method())
print(abc.car())

