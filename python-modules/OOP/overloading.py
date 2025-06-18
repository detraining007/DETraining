
def add(x,y):
        return x + y
def add(x,y,z):
    return x + y + z
# add(4,5)  throws error
add(4,5,6)
'''
There is no overloading in python sice it has no pre defined data types and if we re declare trying to overload
it will update method or variable with latest definition
eg: x = 23
    x = "Apple"
    x = 23 no longer exists
    similarly
    def add(x,y):
        return x + y
    def add(x,y,z):
        return x + y + z
    
    there will be only one add method which takes 3 arguments
    predefined one is updated to new one
'''