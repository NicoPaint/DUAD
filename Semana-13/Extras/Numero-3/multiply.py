from validate_numbers_decorator import validate_numbers
from log_call_decorator import log_call

@validate_numbers
@log_call
def multiply(num1, num2):
    return num1 * num2


try:
    print(f"Resultado: {multiply(6, 8)}")
    print(f"Resultado: {multiply(123, 76)}")
except ValueError as error:
    print(error)