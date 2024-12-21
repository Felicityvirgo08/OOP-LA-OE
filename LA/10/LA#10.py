print("LA#10")

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"My vehicle brand is {self.brand}, the model is {self.model}, and it uses {self.fuel_type} as fuel.")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

toyota = Car("Toyota", "Corolla", "Gasoline")
toyota.describeVehicle()

fazzio = Motorcycle("Fazzio", "Scooter", "Gasoline")
fazzio.describeVehicle()