def count_the_character():
    word = input("Ingrese la palabra que quiere evaluar: ")
    character = input("Ingrese el caracter que quiere encontrar: ")
    
    return count_the_character_int(word, character)


def count_the_character_int(word: str, character: str):

    if not isinstance(word, str) or not isinstance(character, str):
        raise TypeError("Please enter a string only")
    if len(character) != 1 or character == "" or character == " ":
        raise ValueError("Please enter just one valid character")

    counter = 0
    for letter in word:
        if(letter.lower() == character.lower()):
            counter += 1
    
    return f"Se ha encontrado {counter} veces el carácter"