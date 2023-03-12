class Shape:
    def __init__(self,color):
        self.color=color
class Rectangle(Shape):
    def __init__(self, color,width,height):
        super().__init__(color)
        self.width=width
        self.height=height
        
    def display(self):
        print(f'this is the color {self.color} this is the width {self.width} this is the height {self.height}')
        

rect=Rectangle('red',100,200)
rect.display()
        