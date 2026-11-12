'''class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
def make_sound(animal):
    animal.sound()

a1=Dog()
a2=Cat()
make_sound(a1)
make_sound(a2)
a1.sound()
a2.sound()'''

'''def check_age(age):
    if age<18:
        raise ValueError("Age must be 18 or older")
    return True

try:
    check_age(15)
except ValueError as e:
    print(e)'''


'''class Parrot:
    name=""
    age=0

parrot1=Parrot()
parrot1.name="Blue"
parrot1.age=20

parrot2=Parrot()
parrot2.name="Yellow"
parrot2.age=54

print(f"Parrot name is {parrot1.name} and age is {parrot1.age}")
print(f"Parrot name is {parrot2.name} and age is {parrot2.age}")'''

'''class Calculator:
    def calc(self,a,b):
        print(a+b)

cal=Calculator()
sum=cal.calc(1,2)'''

'''class Student:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(f"Student name is {self.name} and age is {self.age}")

detail=Student()
detail.details("Arjun",20)'''

'''class Car:
    def __init__(self,brand,model):
        self._brand=brand
        self._model=model
    def show_info(self):
        print(f"The car brand is {self._brand} and the model is {self._model}")

car1=Car("Toyotta","Corolla")
car1.show_info()'''

'''class Employee:
    def __init__(self,name):
        self._name=name

class Manager(Employee):
    def get_name(self):
        print(f" the name is {self._name}")

emp=Manager("Arjun")
emp.get_name()'''

'''class Employee:
    def __init__(self,name):
        self.__name=name

class Manager(Employee):
    def get_name(self):
        print(f" the name is {self._Employee__name}")

emp=Manager("Arjun")
emp.get_name()'''


'''class BankAccount:
    def __init__(self,accountnumber,balance,pin):
        self.ac=accountnumber
        self._bal=balance
        self.__pin=pin

    def get_balance(self):
        return(self._bal)

    def __check_pin(self,entered_pin):
        return entered_pin==self.__pin

    def withdraw(self,amount,entered_pin):
        if self.__pin==entered_pin:
            if (self._bal>amount) or (self._bal==amount):
                print("withdrawal succesful",amount)
                self._bal-=amount
                print("balance_amount is",self._bal)
            else:
                print("insufficient balance")
        else:
            print("incorrect_pin")

account=BankAccount("12345",2000,3695)
account.withdraw(365,3695)'''

'''from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod

    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("BRoom Broom")
    def stop(self):
        print("clu clu")
ca=Car()
ca.start()'''

'''class Parent:
    def greet(self):
        print("hello parent")
class Child(Parent):
    def greet(self):
        print("hello child")
        super().greet()
c=Child()
c.greet()'''

'''def my_decorator(func):
    def wrapper():
        print("first fn call")
        func()
        print("after fn call")
    return wrapper  # Indented under my_decorator, not wrapper

@my_decorator
def say():
    print("hello")

say()'''

#windows,button,labels,text fields

'''import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("Menu","New file selected")

def open_file():
    messagebox.showinfo("Menu","Open file selected")

def exit_file():
    root.quit()

root=tk.Tk()
root.title("Menu bar example")
root.geometry("300x200")

menubar=tk.Menu(root)
file_menu=tk.Menu(menubar,tearoff=0)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_file)

menubar.add_cascade(label="File",menu=file_menu)

root.config(menu=menubar)
root.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox


def show():
    selected = choice.get()
    messagebox.showinfo("Your selection", f"Selected option: {selected}")


root = tk.Tk()
root.title("Radio Button")
root.geometry("300x200")

choice = tk.StringVar(value="option1")

label = tk.Label(root, text="Choose an option")
label.pack(pady=5)

tk.Radiobutton(root, text="Option 1", variable=choice, value="option1").pack(anchor="w")
tk.Radiobutton(root, text="Option 2", variable=choice, value="option2").pack(anchor="w")
tk.Radiobutton(root, text="Option 3", variable=choice, value="option3").pack(anchor="w")

tk.Button(root, text="Submit", command=show).pack(pady=10)

root.mainloop()'''







