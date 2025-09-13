import json

def add_new_pokemon(file_path):
    
    try:
        pokemon_list = [] #esta lista va a guardar la informacion parseada del JSON

        #Se lee el JSON, se parsea y se guarda la informacion en pokemon_list
        with open(file_path, encoding = "utf-8") as file:
            reader = file.read()
            pokemon_json = reader
            pokemon_list = json.loads(pokemon_json)

        poke_names = [poke["name"]["english"].lower() for poke in pokemon_list] #Se extrae los nombres de los pokemones para poder hacer la evaluacion si ya esta guardados o no

        #Se pide al usuario que agrege el pokemon. Si ya existe dispara un error
        poke_name = input("\nIngrese su nuevo pokémon: ").strip().lower()
        if (poke_name in poke_names):
            raise ValueError("Este pokémon ya esta en la lista, por favor ingrese otro diferente")
        
        #Un pokemon puede tener 1 o 2 tipos, por lo que este bloque permite guardar 2 tipos diferentes de pokemon.
        poke_type = []
        for index in range(2):
            if(index == 0):
                poke_type.append(input(f"Ingrese el tipo de {poke_name}: ").strip().capitalize())
            elif(index == 1):
                second_type = input(f"Si {poke_name} tiene un segundo tipo, por favor ingreselo. Sino, solo oprima espacio: ").strip().capitalize()
                if not second_type:
                    continue
                elif second_type in poke_type:
                    continue
                poke_type.append(second_type)

        #El siguiente bloque pide al usuario que ingrese la informacion numerica del HP, ataque, defensa, etc. Y si el usuario ingresa un número igual o menor a cero o ingresa otro tipo de dato diferente a un int, se dispara un error
        poke_hp = int(input(f"Ingrese el HP de {poke_name}: "))
        if poke_hp <= 0:
            raise ValueError("El HP del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        poke_attack = int(input(f"Ingrese el ataque de {poke_name}: "))
        if poke_attack <= 0:
            raise ValueError("El ataque del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        poke_defense = int(input(f"Ingrese la defensa de {poke_name}: "))
        if poke_defense <= 0:
            raise ValueError("La defensa del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        poke_sp_attack = int(input(f"Ingrese la velocidad de ataque de {poke_name}: "))
        if poke_sp_attack <= 0:
            raise ValueError("La velocidad de ataque del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        poke_sp_defense = int(input(f"Ingrese la velocidad de defensa de {poke_name}: "))
        if poke_sp_defense <= 0:
            raise ValueError("La velocidad de defensa del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        poke_speed = int(input(f"Ingrese la velocidad de {poke_name}: "))
        if poke_speed <= 0:
            raise ValueError("La velocidad del pokémon no puede ser menor a cero, por favor intentelo nuevamente")
        
        #Creamos el dic con la información recolectada del usuario
        new_pokemon = {
            "name": {
                "english": poke_name.capitalize()
            },
            "type": poke_type,
            "base": {
                "HP": poke_hp,
                "Attack": poke_attack,
                "Defense": poke_defense,
                "Sp. Attack": poke_sp_attack,
                "Sp. Defense": poke_sp_defense,
                "Speed": poke_speed,
            }
        }

        pokemon_list.append(new_pokemon) #Agregamos al final de la lista el nueve dic pokemon

        #Finalmente abrimos nuevamente el JSON de pokemones, convertimos la list a formato JSON y reescribimos el archivo JSON con la nueva información
        with open(file_path, mode = "w", encoding = "utf-8") as file:
            new_pokemon_json = json.dumps(pokemon_list, indent = 2)
            file.write(new_pokemon_json)

    #Estos excepts atrapan posibles errores de informacion mal ingresada o que no se encuentre el archivo JSON de pokemones
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except ValueError as error:
        print(error)
    
    
if __name__=="__main__":
    add_new_pokemon("pokemon.json")