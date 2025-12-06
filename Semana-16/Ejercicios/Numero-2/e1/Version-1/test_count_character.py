#Version 1: en esta version se van a crear los test para la funcion count_the_character asi como fue escrita la primera vez (sin refactorizacion)

from count_character import count_the_character #Esta funcion utiliza 2 input en su ejecucion por lo que vamos a utilizar monkeypatch (fixture de pytest) para, que solo durante la ejecucion del test, reemplazar la funcion input() con otra que solo va a devolver los datos de prueba, uno a la vez.
import pytest

def test_count_the_character_returns_the_correct_answer(monkeypatch):
    #Arrange
    # Preparamos un iterador con las respuestas que queremos que input() devuelva
    inputs = iter(["engineer", "e"])
    # Reemplazamos builtins.input por una función lambda que devuelve el siguiente valor del iterador cada vez que se llame
    monkeypatch.setattr("builtins.input", lambda prompt="" : next(inputs))

    #Act
    result = count_the_character()

    #Assert
    assert result == "Se ha encontrado 3 veces el carácter"


def test_count_the_character_throws_a_value_error_when_character_invalid(monkeypatch):
    #Arrange
    inputs = iter(["manzana", "on"])
    monkeypatch.setattr("builtins.input", lambda prompt="" : next(inputs))

    #Act & Assert
    with pytest.raises(ValueError):
        count_the_character()


def test_count_the_character_returns_zero_when_there_is_no_match(monkeypatch):
    #Arrange
    inputs = iter(["Luis", "x"])
    monkeypatch.setattr("builtins.input", lambda prompt="" : next(inputs))

    #Act
    results = count_the_character()

    #Assert
    assert results == "Se ha encontrado 0 veces el carácter"