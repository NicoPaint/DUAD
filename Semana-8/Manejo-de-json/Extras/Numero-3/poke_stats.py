import json

def show_pokemon_stats(file_path):
    
    try:
        with open(file_path, encoding = "utf-8") as file:
            reader = file.read()
            pokemon_list = json.loads(reader)

            poke_names = [pokemon["name"]["english"] for pokemon in pokemon_list]
            poke_stats = [pokemon["base"] for pokemon in pokemon_list]

            for names, stats in zip(poke_names, poke_stats):
                print(f"Name: {names}")
                for keys, values in stats.items():
                    print(f"{keys}: {values}")
                print()

                
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except KeyError as error:
        print(error)
    except AttributeError as error:
        print(error)


if __name__=="__main__":
    show_pokemon_stats("../../Ejercicios/pokemon.json")