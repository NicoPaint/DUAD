my_list = []
has_done = False

while(not has_done):
    my_list.append(input("Ingrese el número a la lista: "))
    user_response = input("¿Terminó de ingresar números a la lista? (s/n)")
    if(user_response == "s" or user_response == "S"):
        has_done = True

my_number = input("Ingrese el número que quiere buscar: ")
contador = 0

for number in my_list:
    if(number == my_number):
        contador += 1

print(f"El número {my_number} aparece {contador} veces")