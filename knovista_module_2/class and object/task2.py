'''TASK2: Create a class Employee with attributes name, id, and salary, and write
methods to display the details.'''

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def show_info(self):
        print(self.name)
        print(self.id)
        print(self.salary)

c1=Employee("Arjun",2,50000)
c1.show_info()