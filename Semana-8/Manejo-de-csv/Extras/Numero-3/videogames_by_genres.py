import csv

def count_videogames_by_genre(file_path):

    genre_count = {}

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
    
            reader = csv.DictReader(file)
            for row in reader:
                if row["Género"] in genre_count:
                    genre_count[row.get("Género")] += 1
                else:
                    genre_count[row.get("Género")] = 1

        print("\nCantidad de videojuegos por género encontrados:\n")
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except KeyError as error:
        print(f"Error: La columna {error} no existe en el archivo CSV.")


if __name__ == "__main__":
    count_videogames_by_genre('../../Ejercicios/Numero-1/videogames.csv')