"""TASK1. Use abc module to create an abstract class Animal with an abstract method speak()."""

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bow Bow")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")


an=[Dog(),Cat()]
for animal in an:
    animal.speak()
