def print_user_info():
    try:
        user_name = input("Please submit your name: ")
        for letter in user_name:
            if(letter.isdigit()):
                raise ValueError("Your name cannot either be or have a number")
        if(user_name == ""):
            raise ValueError("Please type your name")
        
        user_age = input("Please submit your age: ")
        for letter in user_age:
            if(letter.isalpha() or letter == " "):
                raise ValueError("Invalid number")
        if(user_age == ""):
            raise ValueError("Please type your age")
            
        int(user_age)      

        print(f"Hi {user_name}, your age is {user_age}")
    except ValueError as error:
       print(error)

if __name__ == "__main__":
    print_user_info()