class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    

    def get_area(self):
        return self.width * self.height
    

    def get_perimeter(self):
        return 2 * (self.width + self.height)


def get_rectangle_properties():

    try:
        rectangle_width = int(input("Ingrese el ancho: "))
        rectangle_height = int(input("Ingrese la altura: "))
        if rectangle_height < 0 or rectangle_width < 0:
            raise ValueError("Ingresaste un valor negativo, por favor ingresa solo valores positivos")
        
        my_rectangle = Rectangle(rectangle_width, rectangle_height)

        print(my_rectangle.get_area())
        print(my_rectangle.get_perimeter())

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    get_rectangle_properties()