class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculateArea(self):
        return self.width * self.height
    
    
rect=Rectangle(5,7)
print("Area is : ", rect.calculateArea())
        