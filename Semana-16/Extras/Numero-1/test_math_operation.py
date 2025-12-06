from math_operation import MathOperations
import pytest

my_test_object = MathOperations()

def test_math_operation_sum_function_return_correct_answer_with_positive_numbers():
    
    input_number1 = 6
    input_number2 = 3

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.sum()

    assert result == 9


def test_math_operation_sum_function_return_correct_answer_with_negative_numbers():

    input_number1 = -7
    input_number2 = -15

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.sum()

    assert result == -22


def test_math_operation_sum_function_return_correct_answer_with_zeros():

    input_number1 = 0
    input_number2 = 0

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.sum()

    assert result == 0


def test_math_operation_multiply_function_return_correct_answer_with_positive_numbers():
    
    input_number1 = 5
    input_number2 = 8

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.multiply()

    assert result == 40


def test_math_operation_multiply_function_return_correct_answer_with_negative_numbers():

    input_number1 = -3
    input_number2 = 37

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.multiply()

    assert result == -111


def test_math_operation_multiply_function_return_correct_answer_with_zeros():

    input_number1 = 0
    input_number2 = 0

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.multiply()

    assert result == 0


def test_math_operation_division_function_return_correct_answer_with_positive_numbers():
    
    input_number1 = 64
    input_number2 = 8

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.division()

    assert result == 8


def test_math_operation_division_function_return_correct_answer_with_negative_numbers():

    input_number1 = -8
    input_number2 = -2

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    result = my_test_object.division()

    assert result == 4


def test_math_operation_division_function_return_correct_answer_with_zeros():

    input_number1 = 0
    input_number2 = 0

    my_test_object.Number1 = input_number1
    my_test_object.Number2 = input_number2
    
    with pytest.raises(ZeroDivisionError):
        my_test_object.division()