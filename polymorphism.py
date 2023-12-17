# Simple polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    def move(self):
        print("Roll!")


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car = Car("Tesla", "Model S")
boat = Boat("Yacht", "20X")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()

vehicle = Vehicle("Parent brand", "Parent model")
print(vehicle.brand)
print(vehicle.model)
vehicle.move()
