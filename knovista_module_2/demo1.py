'''class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        print("is driving a", self.color, self.name)'''






'''class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d=Dog()
d.sound()'''

'''class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
d=Dog()
c=Cat()
d.sound()
c.sound()'''

'''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area of the circle:", circle.area())'''


'''class Parent:
    def show(self):
        print("This is the parent class.")
class Child(Parent):
    def show(self):
        super().show()
        print("This is the child class.")
c=Child()
c.show()'''

def count(n):
    for i in range(1, n+1):
        yield i

g= count(5)
print(g .__next__())
print(g .__next__())