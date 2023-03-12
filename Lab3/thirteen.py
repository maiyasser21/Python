import math
class Shape:
    def __init__(self,color):
        self.color=color
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, color,width,height):
        super().__init__(color)
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
        
    def display(self):
        print(f'this is the color {self.color} this is the width {self.width} this is the height {self.height}')
        
        
class Circle(Shape):
    def __init__(self, color,raduis):
        super().__init__(color)
        self.raduis=raduis
        
    def area(self):
        return math.pi*self.raduis*self.raduis
    
rect=Rectangle('red',200,100)
c=Circle('blue',5)
print(f"Rectangle Area is {rect.area()} Circle Area is {c.area()}")
    
        