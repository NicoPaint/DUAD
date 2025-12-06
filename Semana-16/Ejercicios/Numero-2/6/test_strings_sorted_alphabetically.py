from strings_sorted_alphabetically import sort_strings_alphabetically
import pytest

def test_sort_strings_alphabetically_returns_expected_result():
    #Arrange
    input_string = "zap-bottle-bag-electrolyte-anniversary-pub-team"
    #Act
    result = sort_strings_alphabetically(input_string)
    #Assert
    assert result == "anniversary-bag-bottle-electrolyte-pub-team-zap"


def test_sort_strings_alphabetically_throws_exception_with_string_separated_by_spaces():
    #Arrange
    input_string = "zap bottle bag electrolyte anniversary pub team"
    #Act & Assert
    with pytest.raises(ValueError):
        sort_strings_alphabetically(input_string)


def test_sort_strings_alphabetically_throws_exception_with_parameter_different_than_string():
    #Arrange
    input_data = ("zap", "bottle", "bag", "electrolyte", "anniversary", "pub", "team")
    #Act & Assert
    with pytest.raises(TypeError):
        sort_strings_alphabetically(input_data)
