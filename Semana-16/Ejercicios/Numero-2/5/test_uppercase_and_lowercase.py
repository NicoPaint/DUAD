from uppercase_and_lowercase import print_uppercase_and_lowercase

def test_print_uppercase_and_lowercase_return_expected_results():
    #Arrange
    input_str = "Best in Class Triple-Walled Insulated Stainless Steel Water Bottle, Keeps your Drinks Cold for up to 24 Hours and Hot for up to 12 Hours, Leak Proof, Make a Difference in the World, White, 17oz"
    #Act
    result = print_uppercase_and_lowercase(input_str)
    #Assert
    assert result == (21, 126)


def test_print_uppercase_and_lowercase_return_just_with_uppercase():
    #Arrange
    input_str = "MOTOCICLETA ELECTRICA"
    #Act
    result = print_uppercase_and_lowercase(input_str)
    #Assert
    assert result == (20, 0)


def test_print_uppercase_and_lowercase_return_just_with_lowercase():
    #Arrange
    input_str = "invente roman, invente"
    #Act
    result = print_uppercase_and_lowercase(input_str)
    #Assert
    assert result == (0, 19)