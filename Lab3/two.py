import math

class Circle:
    def __init__(self,raduis):
        self.raduis=raduis
    def circumference(self):
        return math.pi*2*self.raduis
    

c=Circle(5)
print("Circumference is :",c.circumference())
        
        