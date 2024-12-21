print("LA#11")

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"{self.brand} the model of it is {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

Samsung = Android("Samsung", "S24")
Samsung.describePhone()