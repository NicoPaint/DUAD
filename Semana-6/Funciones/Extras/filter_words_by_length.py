def filter_words_by_length(string_list):
    letter_number = int(input("Ingrese el numero de letras minimas en la palabra: "))

    new_string_list = []

    for string in string_list:
        if(len(string) >= letter_number):
            new_string_list.append(string)
    
    return new_string_list


print(filter_words_by_length(["cielo", "sol", "maravilloso", "día"]))