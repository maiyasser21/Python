class Animal:
    def __init__(self,name):
        self.name=name
        print("Hello from parent class")

class Pet(Animal):
    def __init__(self, name,owner):
        super().__init__(name)
        self.owner=owner
        print("Hello from child constructor")
    def display(self):
        print(f'The Pet name is {self.name} and the owner is {self.owner}')
        
        
cat=Pet("mshmsh","mai")
cat.display()        