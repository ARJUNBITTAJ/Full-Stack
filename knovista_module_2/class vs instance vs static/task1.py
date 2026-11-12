class Demo:
    def __init__(self,x):
        self.x=x

    def instance_method(self):
        print("it is an instance method")

    @classmethod
    def class_method(cls):
        print("it is class method")

    @staticmethod
    def static_method():
        print("it is static method")

obj=Demo(2)
obj.instance_method()
Demo.class_method()
Demo.static_method()
        
