from Shape import Shape

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        return self.perimeter
    
    def calculate_area(self):
        self.area = self.side ** 2
        return self.area
    
my_square = Square(5)
print(my_square.calculate_area())
print(my_square.calculate_perimeter())