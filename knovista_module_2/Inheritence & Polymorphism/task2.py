class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"[{self.brand}] Checking battery and ignition")


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)  
        self.doors = doors

    def start_engine(self):
        super().start_engine() 
        print(f"[{self.brand}] Engine started: Vroom!")


my_car = Car("Toyota", 4)
my_car.start_engine()  