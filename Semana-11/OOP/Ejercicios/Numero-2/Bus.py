class Person:
    pass


class Bus:
    def __init__(self, max_passenger = 3):
        self.passengers = []
        self.max_passengers = max_passenger

    def get_in_passenger(self, person):
        if isinstance(person, Person):
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(person)
                print("Subió una persona")
            else:
                print("El bus esta lleno, no puede subir mas personas")
    

    def get_people_off_the_bus(self):
        if self.passengers:
            self.passengers.pop()
            print("Se bajo una persona")
        else:
            print("El bus ya esta vacío")


my_bus = Bus()
my_bus_2 = Bus()

person1 = Person()
person2 = Person()
person3 = Person()
person4 = Person()


my_bus.get_in_passenger("Persona")
my_bus.get_in_passenger(123)
my_bus.get_in_passenger(person1)
my_bus.get_in_passenger(person2)

my_bus_2.get_in_passenger(person3)
my_bus_2.get_in_passenger(person4)

print(f"Bus 1: {my_bus.passengers}")
print(f"Bus 2: {my_bus_2.passengers}")

my_bus.get_people_off_the_bus()
my_bus.get_people_off_the_bus()
my_bus_2.get_people_off_the_bus()
my_bus_2.get_people_off_the_bus()

