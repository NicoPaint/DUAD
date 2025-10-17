from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        print(f"{self._brand} de {self._year} - Tipo: {self._type}")

my_bike = Motorcycle("Indian", "2025", "muscle")
my_bike.get_info()