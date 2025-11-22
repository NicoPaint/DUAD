def filter_words_by_length(string_list):
    letter_number = int(input("Ingrese el numero de letras minimas en la palabra: "))

    return filter_words_by_length_int(string_list, letter_number)


def filter_words_by_length_int(string_list, letter_number):

    if not isinstance(string_list, list):
        raise TypeError("Please enter a list only")
    if not isinstance(letter_number, int):
        raise TypeError("Please enter a integer only")
    if letter_number < 1 :
        raise ValueError("Please enter a number greater than or equal to 1")

    new_string_list = []

    for string in string_list:
        if(len(string) >= letter_number):
            new_string_list.append(string)
    
    return new_string_list


#print(filter_words_by_length(["cielo", "sol", "maravilloso", "día"]))