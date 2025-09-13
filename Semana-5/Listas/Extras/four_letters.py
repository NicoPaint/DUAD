my_list = []
new_list = []

for index in range(5):
    my_list.append(input(f"Ingrese su palabra número {index + 1}: "))
    if(len(my_list[index]) > 4):
        new_list.append(my_list[index])

print(new_list)

