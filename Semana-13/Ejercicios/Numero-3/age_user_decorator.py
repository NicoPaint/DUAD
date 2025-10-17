from datetime import date

def just_adults(func):
    def wrapper(user, *args):
        if not isinstance(user, User):
            raise ValueError("La funcion debe tener un User como argumento")
        elif user.age < 18:
            raise ValueError("Lo sentimos, el usuario debe ser mayor de edad")
        func(user, *args)
    
    return wrapper


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))
    
    @just_adults
    def withdraw_user_info(self):
        print(f"Aqui esta la información del usuario:")
        print(f"Nombre: {self.name}")
        print(f"Fecha de nacimiento: {self.date_of_birth}")