class Person:
    def __init__(self,name,age):
        print("This is the constructor")
        self.name=name
        self.age=age
    def __del__(self):
        print("This is the destructor")


p=Person("mai",23)
