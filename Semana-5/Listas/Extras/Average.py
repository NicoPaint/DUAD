mi_lista = [10, 20, 30, 40, 50]
new_list = []
acumulador = 0
promedio = 0

for number in mi_lista:
    acumulador += number
    
if(len(mi_lista) > 0):
    promedio = acumulador/len(mi_lista)

print(f"Promedio {promedio}")

for number in mi_lista:
    if(number > promedio):
        new_list.append(number)

print(f"Nueva lista: {new_list}")