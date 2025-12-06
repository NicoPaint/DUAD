def count_vowels(string):

    if not isinstance(string, str):
        raise TypeError("Please enter a string only")

    vowels_number = 0

    for letter in string.lower():
        if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            vowels_number += 1
    

    return vowels_number

#print(count_vowels("Hola mundo"))