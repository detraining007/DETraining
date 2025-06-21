class student(object):
    def __init__(self):
        self.name = "rakesh"
        self.marks = 20

    def getter(self):
        return self.name, self.marks

    def __add__(self, other):
        
        total_marks = self.marks + other.marks
        return total_marks

if __name__ == "__main__":
    obj1 = student()
    obj2 = student()
    print("Total Marks:", obj1 + obj2)  
