def all_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, list):
                for item in arg:
                    if not isinstance(item, (int, float)):
                        raise ValueError("Los parametros de la función deben ser números (lista)")
            elif isinstance(arg, dict):
                for value in arg.values():
                    if not isinstance(value, (int, float)):
                        raise ValueError("Los parametros de la función deben ser números (dict)")
            elif not isinstance(arg, (int, float, range)):
                raise ValueError("Los parametros de la función deben ser números")
        for values in kwargs.values():
            if isinstance(values, list):
                for item in values:
                    if not isinstance(item, (int, float)):
                        raise ValueError("Los parametros de la función deben ser números (lista)")
            elif isinstance(values, dict):
                for value in values.values():
                    if not isinstance(value, (int, float)):
                        raise ValueError("Los parametros de la función deben ser números (dict)")
            elif not isinstance(values, (int, float, range)):
                raise ValueError("Los parametros de la función deben ser números")
        return func(*args, **kwargs)

    return wrapper

@all_numbers
def print_numbers(numbers):
    if isinstance(numbers, dict):
        for number in numbers.values():
            print(f"Número: {number}")
        return
    for number in numbers:
        print(f"Número: {number}")

@all_numbers
def return_all_doubles(*args):
    double_list = [n * 2 for n in args]
    return double_list

try:
    print_numbers(range(1,21))
    print_numbers([1, 2, 3, 4])
    print_numbers({"first":1, "second":3, "third":5})
    print(return_all_doubles(1,5,3,6,7,3,45))
except ValueError as error:
    print(error)