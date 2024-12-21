print("LA#21")

class Adobo:
    def __init__(self, chicken, soysauce, vinegar, potato, rekados):
        self.__chicken = chicken
        self.__soysauce = soysauce
        self.__vinegar = vinegar
        self.__potato = potato
        self.__rekados = rekados

    def __str__(self):
        return f"My Adobo has {self.__chicken}, {self.__soysauce}, {self.__vinegar}, {self.__potato}, and {self.__rekados}"

    def may_chicken_ba(self, age):
        if age <= 100:
            return self.__chicken
        else:
            return "Secret"

    def i_set_to(self, bago):
        self.__chicken = bago

# Creating an instance of Adobo
adobong_chicken = Adobo("sliced chicken", "soysauce", "vinegar", "potato", "rekados")

# Modifying the __chicken attribute using the i_set_to method
adobong_chicken.i_set_to("hiniwang putatu")

# Checking the result after modifying the chicken attribute
print(adobong_chicken.may_chicken_ba(31))