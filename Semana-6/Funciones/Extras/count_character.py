def count_the_character():
    word = input("Ingrese la palabra que quiere evaluar: ")
    character = input("Ingrese el caracter que quiere enxontrar: ")

    counter = 0

    for letter in word:
        if(letter == character):
            counter += 1
    
    return f"Se ha encontrado {counter} veces el carácter"


print(count_the_character())