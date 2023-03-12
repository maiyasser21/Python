class Animal:
    def __init__(self,name):
        self.name=name
        print("Hello from parent class")

class Pet:
    def __init__(self,owner):
        self.owner=owner
        print("Hello from child constructor")
    def display(self):
        print(f'the owner is {self.owner}')
        
class Dog(Animal,Pet):
    def __init__(self, name,owner,breed):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        self.breed=breed
    def show(self):
        print(f'The dog name is {self.name} the owner is {self.owner} the breed is {self.breed}')


dog=Dog("rex","ahmed","mm")
dog.show()        