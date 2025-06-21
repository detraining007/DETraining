class mother:
    mother_name = "mother"
    def mother_(self):
        print(self.mother_name)

class father:
    father_name = "father"
    def father_(self):
        print(self.father_name)

class son(mother, father):
    def parent_(self):
        print("father", self.father_name) 
        print("mother", self.mother_name)

s1 = son()
s1.mother_name = "laxmi"
s1.father_name = "raju"
s1.parent_()
