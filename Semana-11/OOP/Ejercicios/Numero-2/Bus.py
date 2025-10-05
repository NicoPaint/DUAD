class Person:
    pass


class Bus:
    max_passengers = 3
    passengers = []

    def get_in_passenger(self, person):
        if isinstance(person, Person):
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(person)
            else:
                print("El bus esta lleno, no puede subir mas personas")
    

    def get_people_off_the_bus(self):
        if self.passengers:
            self.passengers.pop()
        else:
            print("El bus ya esta vacío")


my_bus = Bus()

person1 = Person()
person2 = Person()
person3 = Person()
person4 = Person()


my_bus.get_in_passenger(person1)
my_bus.get_in_passenger("Persona")
my_bus.get_in_passenger(123)
my_bus.get_in_passenger(person2)
my_bus.get_in_passenger(person3)
my_bus.get_in_passenger(person4)

my_bus.get_people_off_the_bus()
my_bus.get_people_off_the_bus()
my_bus.get_people_off_the_bus()
my_bus.get_people_off_the_bus()

