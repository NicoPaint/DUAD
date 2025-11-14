def twist_string(my_string):

    if not isinstance(my_string, str):
        raise TypeError("El argumento debe ser un string")

    twisted_string = ""
    for index in range(len(my_string) - 1, -1, -1):
        twisted_string += my_string[index]
    
    return twisted_string


print(twist_string("Hamburguesa con papas"))