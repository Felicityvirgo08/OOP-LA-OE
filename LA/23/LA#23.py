print("LA#23")

class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing....")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper

killua = AnimeCharacter("Killua", "Electric shock")

@killua.introduce
def character_intro():
    print(f"I am {killua.name} and I can use {killua.ability}.")

character_intro()