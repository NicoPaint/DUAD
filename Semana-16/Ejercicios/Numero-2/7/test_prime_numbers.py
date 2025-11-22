from prime_numbers import find_prime_numbers
import pytest

def test_find_prime_numbers_returns_correct_prime_numbers():
    #Arrange
    input_list = [4, 5, 7, 13, 1, 1, 24, 47, 32, 11, 66, 97]
    #Act
    results = find_prime_numbers(input_list)
    #Assert
    assert results == [5, 7, 13, 1, 1, 47, 11, 97]


def test_find_prime_numbers_returns_an_empty_list_when_there_is_no_primes():
    #Arrange
    input_list = [4, 24, 32, 66, 100]
    #Act
    results = find_prime_numbers(input_list)
    #Assert
    assert results == []


def test_find_prime_numbers_throws_exception_with_parameters_different_than_a_list():
    #Arrange
    input_data = 123
    #Act & Assert
    with pytest.raises(TypeError):
        find_prime_numbers(input_data)