import time
class Circle:
    pie = 3.14
    def __init__(self, radius):
        self.radius = radius
         
    
    def circumference(self):
        return 2*Circle.pie*self.radius
    
obj1 = Circle(4)
print(obj1.circumference())

