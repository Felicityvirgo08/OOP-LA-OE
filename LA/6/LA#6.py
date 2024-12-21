print("LA#6")

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def laptop_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


student = Laptop("Asus" , "Macbook")
print(student.laptop_info())