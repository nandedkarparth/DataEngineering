class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car(make="Toyota", model="Camry")
print(f"My car is a {my_car.make} {my_car.model}.")
