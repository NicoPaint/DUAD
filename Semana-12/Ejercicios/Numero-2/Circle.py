from Shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return round(self.perimeter, 3)
    
    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
        return round(self.area, 3)
    
my_circle = Circle(5)
print(my_circle.calculate_area())
print(my_circle.calculate_perimeter())