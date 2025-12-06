from twist_string import twist_string
import pytest


def test_twist_string_returns_correct_string():
    #Arrange
    input_str = "Prueba este string"
    #Act
    result = twist_string(input_str)
    #Assert
    assert result == "gnirts etse abeurP"


def test_twist_string_works_with_empty_string():
    #Arrange
    input_str = ""
    #Act
    result = twist_string(input_str)
    #Assert
    assert result == ""


def test_twist_string_throws_exception_with_parameter_different_than_string():
    #Arrange
    input_str = ["Jennifer", "Silvia", "Valentina"]
    with pytest.raises(TypeError):
        twist_string(input_str)