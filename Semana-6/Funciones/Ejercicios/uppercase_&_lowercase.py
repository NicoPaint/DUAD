def print_uppercase_and_lowercase(my_string):
    total_uppercases = 0
    total_lowercases = 0

    for letter in my_string:
        if(letter.isupper()):
            total_uppercases += 1
        elif(letter.islower()):
            total_lowercases += 1
    
    print(f"There are {total_uppercases} upper cases and {total_lowercases} lower cases")


print_uppercase_and_lowercase("I love Nación Sushi")