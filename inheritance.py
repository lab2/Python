# Simple inheritance

class Truck:
    def __init__(self, model, weight, wheel):
        self.model = model
        self.weight = weight
        self.wheel = wheel

    def conftype(self):
        return f"{self.model} has a V12 model"

    def wheels(self, wheel):
        return f"{self.wheel} wheels\n"


class UStruck(Truck):
    def conftype(self):
        return f"{self.model} has a special US model"


class EUtruck(Truck):
    def wheels(self):
        return "8 wheels\n"


class CHtruck(Truck):
    def wheels():
        return EUtruck.wheels()


ustruck = Truck("Ford", 120, "18")
print(ustruck.model)
print(ustruck.weight)
print(ustruck.conftype())
print(ustruck.wheels("4"))

txtruck = UStruck("Silverado", 80, "13")
print(txtruck.model)
print(txtruck.weight)
print(txtruck.conftype())
print(txtruck.wheels("4"))

eutruck = EUtruck("Iveco", 80, str())
print(eutruck.model)
print(eutruck.weight)
print(eutruck.conftype())
print(eutruck.wheels())

chtruck = EUtruck("Saurer", 90, str())
print(chtruck.model)
print(chtruck.weight)
print(chtruck.conftype())
print(chtruck.wheels())
