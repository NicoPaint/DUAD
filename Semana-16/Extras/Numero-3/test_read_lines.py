from read_lines import read_lines
from unittest.mock import mock_open, patch
import pytest


def test_read_lines_return_correct_text_content():
    
    input_file = mock_open(read_data = "Este es el contenido del archivo falso")

    with patch("builtins.open", input_file):
        result = read_lines("directory/excercises/test.txt")
    
    assert result == ["Este es el contenido del archivo falso"]


def test_read_lines_throws_an_FileNotFoundError_exception():

    with patch("builtins.open", side_effect = FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("text.txt")

