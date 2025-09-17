import json

def filter_by_pokemon_type(file_path):
    
    try:
        user_pokemon_type = input("Ingrese el tipo de pokemon que desee filtrar: ").strip().capitalize()

        with open(file_path, encoding = "utf-8") as file:
            reader = file.read()
            pokemon_list = json.loads(reader)

            # retorna y guarda los pokemones que sean del tipo que pidío el usuario
            filtered_pokemons = [pokemon["name"]["english"] for pokemon in pokemon_list if user_pokemon_type in pokemon['type']]

            if filtered_pokemons:
                print("Los pokemos que existen de ese tipo son: ")
                for pokemon in filtered_pokemons:
                    print(pokemon)
            else:
                print("Lo sentimos, pero no tenemos ningún Pokémon con ese tipo. Intentelo nuevamente.")
                
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except ValueError as error:
        print(error)
    except KeyError as error:
        print(error)
    except AttributeError as error:
        print(error)


if __name__=="__main__":
    filter_by_pokemon_type("../../Ejercicios/pokemon.json")