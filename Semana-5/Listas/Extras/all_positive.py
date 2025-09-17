my_list = [3, 6, 0, -2, 4]

for index, number in enumerate(my_list):
    if(number <= 0):
        print("Hay al menos un número negativo o cero")
        break
    if(index == len(my_list) - 1):
        print("Todos son positivos")
