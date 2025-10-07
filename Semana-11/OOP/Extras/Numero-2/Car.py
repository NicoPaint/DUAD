class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    
    def accelerate(self, amount):
        self.speed = amount
    

    def brake(self, amount):
        if amount > self.speed:
            self.speed = 0
        else:
            self.speed -= amount
    

    def __str__(self):
        return f"{self.brand} {self.model} - velocidad {self.speed} km/h"
    

my_car = Car("Nissan", "Ariya")
my_car.accelerate(130)
my_car.brake(100)
my_car.brake(40)
print(my_car)