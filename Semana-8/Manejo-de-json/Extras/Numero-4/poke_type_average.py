import json

def calculate_pokemon_type_avg(file_path):
    
    try:
        with open(file_path, encoding = "utf-8") as file:
            reader = file.read()
            pokemon_list = json.loads(reader)

            type_avg_dict = {} # Este dict va a almacenar la información de los promedio por tipo

            # Se recorren cada uno de los pokemones en la lista "pokemon_list" para utilizar su información
            for pokemon in pokemon_list:
                # Se calcula y se guarda el promedio de nivel del pokemon
                poke_avg = 0
                accumalator = 0
                for key, value in pokemon["base"].items():
                    if key == "HP":
                        continue
                    else:
                        accumalator += value
                poke_avg = accumalator / (len(pokemon["base"].values()) - 1)

                # Se recorre la lista type del pokemon para registrar el tipo en el dict "type_avg_dict" y agregar el promedio sino existe. Y si ya esta agregado, se recalcula el promedio sin duplicar el tipo en el dict
                for type in pokemon['type']:
                    if type in type_avg_dict.keys():
                        pre_step = type_avg_dict[type]["poke_avg"] * type_avg_dict[type]["pokemons"]
                        type_avg_dict[type]["pokemons"] += 1
                        type_avg_dict[type]["poke_avg"] = (pre_step + poke_avg) / type_avg_dict[type]["pokemons"]
                    else:
                        type_avg_dict[type] = {
                            "poke_avg": poke_avg,
                            "pokemons": 1,
                            }
            
            for key, value in type_avg_dict.items():
                print(f"Tipo: {key} -> Promedio de nivel: {value["poke_avg"]}")
                
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except KeyError as error:
        print(error)
    except AttributeError as error:
        print(error)


if __name__=="__main__":
    calculate_pokemon_type_avg("../../Ejercicios/pokemon.json")