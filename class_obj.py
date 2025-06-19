# Defining a class with __new__ and __init__
class Car:
    def __new__(cls, brand, model):
        print("Creating a new Car instance...")
        return super().__new__(cls)  # Calls the parent class's __new__

    def __init__(self, brand, model):
        print("Initializing the Car instance...")
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand:
            self._brand = new_brand
        else:
            raise ValueError("Brand name must be a non-empty string")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str) and new_model:
            self._model = new_model
        else:
            raise ValueError("Model name must be a non-empty string")

    def display_info(self):
        return f"This car is a {self.brand} {self.model}"


# Creating an object
my_car = Car("Toyota", "Corolla")

# Output:
# Creating a new Car instance...
# Initializing the Car instance...

print(my_car.display_info())  # This car is a Toyota Corollas