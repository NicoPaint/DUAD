from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
    
    def calculate_area(self):
        self.area = self.width * self.height
        return self.area
    
my_rectangle = Rectangle(7, 33)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())