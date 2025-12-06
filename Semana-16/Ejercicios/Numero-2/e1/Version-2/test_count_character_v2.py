#Version 2: en esta version se van a refactorizar la funcion count_the_character (separar la logica de la UI) para asi construir test unitarios mas faciles de mantener y entender.

from count_character_v2 import count_the_character_int
import pytest

def test_count_the_character_returns_the_correct_answer():
    #Arrange
    input_string = "Engineer"
    input_character = "e"
    
    #Act
    result = count_the_character_int(input_string, input_character)

    #Assert
    assert result == "Se ha encontrado 3 veces el carácter"


def test_count_the_character_throws_a_value_error_when_character_invalid():
    #Arrange
    input_string = "manzana"
    input_character = "on"
    
    #Act & Assert
    with pytest.raises(ValueError):
        count_the_character_int(input_string, input_character)


def test_count_the_character_returns_zero_when_there_is_no_match():
    #Arrange
    input_data = 556 
    input_character = "x"

    #Act & Assert
    with pytest.raises(TypeError):
        count_the_character_int(input_data, input_character)
    
    