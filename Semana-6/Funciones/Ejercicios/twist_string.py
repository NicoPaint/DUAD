def twist_string(my_string):
    twisted_string = ""
    for index in range(len(my_string) - 1, -1, -1):
        twisted_string += my_string[index]
    
    return twisted_string


print(twist_string("Hamburguesa con papas"))