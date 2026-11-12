'''TASK2. Implement multiple child classes Dog, Cat, and override speak() method.'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} Bow"


class Cat(Animal):
    def speak(self):
        return f"{self.name} Meow"



pets = [Dog("Rocky"), Cat("kitty")]

for pet in pets:
        print(pet.speak())