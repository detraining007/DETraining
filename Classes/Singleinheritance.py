class Main_class:
    def method_01(self):
        return "This is Method_01 of Main class"
    def method_03(self):
        return "This"
            
class derived_Class(Main_class):
    def Method_02(self):
        return "This is method_02"

obj=derived_Class()
print(obj.Method_02())
print(obj.method_01())
print(obj.method_03())


