class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
    
    def get_info(self):
        print(f"{self._brand} de {self._year}")

my_vehicle = Vehicle("Boeing", "1996")
my_vehicle.get_info()