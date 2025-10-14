def function_data(func):
    def wrapper(*args):
        result = func(*args)
        print(*args)
        print(result)

    return wrapper


@function_data
def get_full_name(first_name, last_name):
    return f"Your full name is: {first_name} {last_name}"


@function_data
def sum_all_numbers(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5


get_full_name("Natalia", "Echeverria")
sum_all_numbers(4,6,9,2,4)