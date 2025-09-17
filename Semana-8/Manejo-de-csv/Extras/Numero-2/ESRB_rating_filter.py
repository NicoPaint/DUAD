import csv

def filter_by_esrb_rating(videogames):
    try:
        user_rating = input("Ingrese la clasificación ESRB que desea filtrar (E, T, M, A): ").strip().upper()
        if user_rating not in ['E', 'T', 'M', 'A']:
           raise ValueError("Clasificación ESRB inválida. Por favor ingrese E, T, M o A.")

        with open(videogames, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            filtered_games = [game for game in reader if game["Clasificación ESRB"].startswith(user_rating)] #list comprehension
            print(f"\nJuegos con clasificación ESRB '{user_rating}':\n")
            if not filtered_games:
                print("No se encontraron juegos con esa clasificación.")
            else:
                for game in filtered_games:
                    print(f"Nombre: {game["Nombre"]}")
                    print(f"Género: {game["Género"]}")
                    print(f"Desarrollador: {game["Desarrollador"]}")
                    print(f"Clasificación ESRB: {game["Clasificación ESRB"]}")
                    print("-" * 40)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    filter_by_esrb_rating('../../Ejercicios/Numero-1/videogames.csv')