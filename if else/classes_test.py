# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The {self.brand} engine has started-parent.")

# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling the parent class init method
        self.model = model

    def start_engine(self):
        super().start_engine()  # Calling the parent class method
        print(f"The {self.brand} {self.model} engine is running.-child")

# Creating instances of the classes
vehicle = Vehicle("Generic Vehicle-parent")
vehicle.start_engine()  # Output: The Generic Vehicle engine has started.
car = Car("Toyota-c", "Corolla-c")
car.start_engine()  # Output: The Toyota engine has started. -The Toyota Corolla engine is running.
