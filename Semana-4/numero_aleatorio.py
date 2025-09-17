import random

random_number = random.randint(1, 10)
user_number = int(input("Ingrese el numero secreto: "))

while(user_number != random_number):
    user_number = int(input("No es el número, ingreselo nuevamente: "))

print("¡Feliciationes! encontraste el número secreto")