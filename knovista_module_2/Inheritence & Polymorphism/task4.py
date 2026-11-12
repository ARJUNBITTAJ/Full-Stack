'''TASK4: Write a class hierarchy for Shape → Rectangle, Circle, each having area()
method'''

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)



shapes = [
    Rectangle(width=10, height=5),
    Circle(radius=7)
]

for s in shapes:
    print(f"{s.__class__.__name__} Area: {s.area():.2f}")