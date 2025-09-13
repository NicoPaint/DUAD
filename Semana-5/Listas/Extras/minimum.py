my_list = [9, 4, 7, 1, 5]
minimo = my_list[0]

for number in my_list:
    if(minimo > number):
        minimo = number

print(f"El menor valor es {minimo}")

