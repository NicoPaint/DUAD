def add_values(list):
    accumulator = 0

    for item in list:
        try:
            accumulator += float(item)
            print(f"{item} sumado correctamente")
        except ValueError:
            print(f"Elemento invalido: '{item}'")
    
    print(f"Total de la suma: {accumulator}")


my_list = ['10', 'manzana', '5.5', '3', 'n/a']
add_values(my_list)