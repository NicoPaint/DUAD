from sum_number_list import sum_all_numbers
import pytest

def test_sum_number_list_returns_correct_sum():
    #Arrange
    input_list = [6, 8, 3, 1 ,5]
    #Act
    result = sum_all_numbers(input_list)
    #Assert
    assert result == 23


def test_sum_number_list_works_with_empty_list():
    #Arrange
    input_list = []
    #Act
    result = sum_all_numbers(input_list)
    #Assert
    assert result == 0


def test_sum_number_list_throw_exception_with_parameters_different_than_a_list():
    #Arrange
    input_list = { "Ejemplo": 123 }
    #Act & Assert
    with pytest.raises(TypeError):
        sum_all_numbers(input_list)