class Vehicle:
    def __init__(self,speed):
        self.speed=speed
        print("Parent class constrctor")

class Car(Vehicle):
    def __init__(self, speed,brand):
        super().__init__(speed)
        self.brand=brand
        print("Child class constructor")
    def getBrand(self):
        return self.brand
    def getSpeed(self):
        return self.speed
    
    
car=Car(1000,"mm")
print(f"Speed is: {car.getSpeed()} and brand is: {car.getBrand()}")
        
    
    
        