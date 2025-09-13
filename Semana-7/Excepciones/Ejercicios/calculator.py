def add(a, b):
     return a + b


def subtract(a, b):
     return a - b


def multiply(a, b):
     return a * b


def divide(a, b):
     return a / b


def calculator():
    current_number = 0
    running = True

    while(running):
        try:
            print(f"Current number = {current_number}")
            operation = input("Type the operation: 'a' for addition; 's' for substracion; 'm' for multiplication; 'd' for division; 'e' for erase, or 'q' to quit the app: ")
            if (operation != "a" and operation != "s" and operation != "m" and operation != "d" and operation != "e" and operation != "q"):
                 raise ValueError('Wrong character selected')
            elif(operation == "e"):
                 current_number = 0
                 continue
            elif(operation == "q"):
                 print("See you next time!")
                 break
            
            operating_number = float(input(f"Type your operating number: "))

            if(operation == "a"):
                 current_number = add(current_number, operating_number)
            elif(operation == "s"):
                 current_number = subtract(current_number, operating_number)
            elif(operation == "m"):
                 current_number = multiply(current_number, operating_number)
            elif(operation == "d"):
                try:
                    current_number = divide(current_number, operating_number)
                except ZeroDivisionError as error:
                     print(f"Error: {error}, try again")

        except ValueError as error:
             print(f"Error: {error}, try again")
	

if __name__ == '__main__':
	calculator()