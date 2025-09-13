import json

def show_pokemon_content(file_path):
    
    try:
        with open(file_path, encoding = "utf-8") as file:
            reader = file.read()
            pokemon_list = json.loads(reader)

            number_list = 1
            for pokemon in pokemon_list:
                print(f"Pokémon número {number_list}")
                for keys, values in pokemon.items():
                    if isinstance(values, dict):  # Evalua si es un dicccionario
                        print(f"{keys}: ", end =" ")
                        for attribute, info in values.items():
                            if attribute.lower() == "english":
                                print(f"\t{info}")
                            else:
                                print(f"\t{attribute} = {info}")
                    elif isinstance(values, list):  # Evalua si es una lista
                        print(f"{keys}: ", end ="\t")
                        for index, info in enumerate(values):
                            if index == len(values) - 1:
                                print(info)
                                break
                            print(f"{info},", end = " ")
                print()
                number_list += 1
                
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except KeyError as error:
        print(error)


if __name__=="__main__":
    show_pokemon_content("../../Ejercicios/pokemon.json")