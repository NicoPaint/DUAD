def convert_to_int(list):
    integers = []

    for item in list:
        try:
            integers.append(int(item))
            print(f"'{item}' convertido a {int(item)}")
        except ValueError:
            print(f"No se pudo convertir el elemento: '{item}'")

    return integers

my_list = ['4', 'hola', '10', '5.2']
convert_to_int(my_list)