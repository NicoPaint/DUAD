from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        print(f"{self._brand} de {self._year} con {self._doors} puertas")

my_car = Car("Nissan", "2023", 4)
my_car.get_info()