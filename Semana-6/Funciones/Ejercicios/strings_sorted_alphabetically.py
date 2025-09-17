def sort_strings_alphabetically(hyphenated_strings):
    string_list = []
    string = ""

    for index, letter in enumerate(hyphenated_strings):
        if(letter == " "):
            return "Please use a hyphenated string only"
        elif(letter == "-"):
            string_list.append(string)
            string = ""
            continue
        elif(index == len(hyphenated_strings) - 1):
            string += letter
            string_list.append(string)
            string = ""
            break
        
        string += letter
    
    string_list.sort()

    for index, word in enumerate(string_list):
        if(index == len(string_list) - 1):
            string += word
            break

        string += f"{word}-"
    
    return string


print(sort_strings_alphabetically("python-variable-funcion-computadora-monitor"))
        

    
