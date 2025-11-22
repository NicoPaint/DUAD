from filter_words_by_length import filter_words_by_length_int
import pytest


def test_filter_words_by_length_int_returns_correct_list():
    input_list = ["cielo", "sol", "maravilloso", "día"]
    input_number = 4

    result = filter_words_by_length_int(input_list, input_number)

    assert result == ["cielo", "maravilloso"]


def test_filter_words_by_length_int_throws_TypeError_argument_different_than_a_list():
    input_data = {"cielo": 234, "sol": 123, "maravilloso": 567, "día": 789}
    input_number = 4

    with pytest.raises(TypeError):
        filter_words_by_length_int(input_data, input_number)


def test_filter_words_by_length_int_throws_ValueError_with_numbers_less_than_1():
    input_list = ["cielo", "sol", "maravilloso", "día"]
    input_number = 0

    with pytest.raises(ValueError):
        filter_words_by_length_int(input_list, input_number)