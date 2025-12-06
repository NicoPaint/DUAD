from divide import divide
import pytest


def test_divide_returns_number_correctly():
    input_number_1 = 10
    input_number_2 = 2

    result = divide(input_number_1, input_number_2)
    assert result == 5


def test_divide_throws_valueError_with_division_by_zero():
    input_number_1 = 10
    input_number_2 = 0

    with pytest.raises(ValueError):
        divide(input_number_1, input_number_2)


def test_divide_throws_typeError_with_division_by_string():
    input_number = 10
    input_string = "Mac Book"

    with pytest.raises(TypeError):
        divide(input_number, input_string)