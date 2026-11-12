from abc import ABC, abstractmethod
class Shape( ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

radius=Circle(5)
print("Area of the circle:",radius.area())