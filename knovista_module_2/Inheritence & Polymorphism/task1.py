'''TASK1: Create a base class Vehicle and derive Car and Bike classes with overridden
start_engine() method.'''

class Vehicle:
    def start_engine(self):
        print("Starting vehicle engine...")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine starts: Vroom vroom!")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine starts: Braap braap!")


vehicles = [Car(), Bike()]
vehicles[0].start_engine()