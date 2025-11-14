from bubble_sort import bubble_sort
import pytest
import random

def test_bubble_sort_returns_sorted_list_with_a_small_list():
    # Arrange
    input_list = [5, 6, 7, 8, 2, 4, 5, 9]
    # Act
    bubble_sort(input_list)
    # Assert
    assert input_list == [2, 4, 5, 5, 6, 7, 8, 9]


def test_bubble_sort_returns_sorted_list_with_a_big_list_more_than_100_items():
    # Arrange
    input_list = random.sample(range(0, 500), 100)
    excepted_result = sorted(input_list)
    # Act
    bubble_sort(input_list)
    # Assert
    assert input_list == excepted_result


def test_bubble_sort_returns_sorted_list_with_a_empty_list():
    # Arrange
    input_list = []
    # Act
    bubble_sort(input_list)
    # Assert
    assert input_list == []


def test_bubble_sort_throws_exception_with_parameters_different_than_a_list():
    #Arrange
    input_list = "Test"
    #Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(input_list)