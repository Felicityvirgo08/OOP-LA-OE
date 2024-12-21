print("LA#9")

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This car is a {self.brand}"

Kotsi = Car("Toyota")
print(Kotsi)
del Kotsi
print(Kotsi)