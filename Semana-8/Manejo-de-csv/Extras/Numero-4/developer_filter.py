import csv

def filter_by_developer(file_path):

    try:
        user_developer = input("Ingrese el nombre del desarrollador que desea filtrar: ").strip().lower()

        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            filtered_games = [game for game in reader if game["Desarrollador"].strip().lower() == user_developer]
            
            print(f"\nVideojuegos desarrollados por '{user_developer}':\n")
            for game in filtered_games:
                print(f"- {game["Nombre"]} (Clasificación: {game["Clasificación ESRB"]}, Género: {game["Género"]})")
                print()

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except KeyError as error:
        print(f"Error: La columna {error} no existe en el archivo CSV.")


if __name__ == "__main__":
    filter_by_developer('../../Ejercicios/Numero-1/videogames.csv')