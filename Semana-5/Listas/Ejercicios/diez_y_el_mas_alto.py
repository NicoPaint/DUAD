user_list = []
mayor = 0

for index in range(10):
    number = int(input(f"Ingrese el {index + 1}°: "))
    user_list.append(number)
    if(index == 0):
        mayor = number
    elif(number > mayor):
        mayor = number

print(f"{user_list}. El más alto fue {mayor}")