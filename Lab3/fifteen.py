class Animal:
    def __init__(self):
        pass
    
    def speak():
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def speak(self):
        return "Bark"
        
        
class Cat(Animal):
    def __init__(self):
        super().__init__()
        
    def speak(self):
        return "Meow"
        
cat=Cat()
dog=Dog()
print(f'Cat is {cat.speak()}ing and dog is {dog.speak()}ing')
        