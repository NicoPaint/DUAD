from age_user_decorator import just_adults, User
from datetime import date

@just_adults
def open_file(user, file_path):
    with open(file_path, mode ="r", encoding="utf-8") as file:
        print(f"{user.name} aqui esta la información del documento:")
        print(file.read())


alejo = User("Alejo", date(2015, 11, 8))
patricia = User("Patricia", date(1968, 6, 2))

try:
    print(f"{alejo.name}: {alejo.age} años")
    print(f"{patricia.name}: {patricia.age} años")
    print()
    """ open_file(alejo, "./test_file.txt") """
    open_file(patricia, "./test_file.txt")
    """ open_file(["alejo"], "./test_file.txt") """
    """ alejo.withdraw_user_info() """
    print()
    patricia.withdraw_user_info()
except ValueError as error:
    print(error)