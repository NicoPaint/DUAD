from count_vowels import count_vowels
import pytest


def test_count_vowels_counts_correctly():
    input_string = "A person who does magic"

    result = count_vowels(input_string)

    assert result == 8


def test_count_vowels_throws_TypeError_with_data_different_than_string():
    input_data = None

    with pytest.raises(TypeError):
        count_vowels(input_data)


def test_count_vowels_works_with_empty_string():
    input_string = ""

    result = count_vowels(input_string)

    assert result == 0