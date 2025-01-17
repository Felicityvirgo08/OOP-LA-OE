print("LA#15")

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Dog: Bark!")

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Cat: Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Bird: Chirp!")

class Fish:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Fish: ...")

def animal_sounds(animal):
    animal.speak()

dog = Dog("Bantay")
cat = Cat("Luna")
bird = Bird("Tweety")
fish = Fish("Nemo")

animals = [dog, cat, bird, fish]

for animal in animals:
    animal_sounds(animal)