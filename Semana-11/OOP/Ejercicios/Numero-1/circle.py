class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0

    
    def get_area(self):
        self.area = 3.1416 * self.radius**2 / 2
        return self.area
    
my_circle = Circle(2**(1/2))
print(my_circle.get_area())