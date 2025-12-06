def count_the_character():
    word = input("Ingrese la palabra que quiere evaluar: ").lower()

    character = input("Ingrese el caracter que quiere encontrar: ").lower()
    if len(character) != 1 or character == "" or character == " ":
        raise ValueError("Please enter just one valid character")

    counter = 0

    for letter in word:
        if(letter == character):
            counter += 1
    
    return f"Se ha encontrado {counter} veces el carácter"