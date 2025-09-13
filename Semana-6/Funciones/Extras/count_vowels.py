def count_vowels(string):
    vowels_number = 0

    for letter in string:
        if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            vowels_number += 1
    

    return vowels_number

print(count_vowels("Hola mundo"))