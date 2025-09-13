import csv

""" videogames = [
  {
    "Nombre": "The Sims",
    "Género": "Simulación de vida",
    "Desarrollador": "Maxis",
    "Clasificación ESRB": "T (Teen)"
  },
  {
    "Nombre": "Diablo II",
    "Género": "Action RPG",
    "Desarrollador": "Blizzard North",
    "Clasificación ESRB": "M (Mature)"
  },
  {
    "Nombre": "Counter-Strike",
    "Género": "Shooter en primera persona",
    "Desarrollador": "Valve",
    "Clasificación ESRB": "M (Mature)"
  },
  {
    "Nombre": "Tony Hawk's Pro Skater 2",
    "Género": "Deportes / Skateboarding",
    "Desarrollador": "Neversoft",
    "Clasificación ESRB": "T (Teen)"
  },
  {
    "Nombre": "Final Fantasy IX",
    "Género": "JRPG",
    "Desarrollador": "Square",
    "Clasificación ESRB": "T (Teen)"
  },
  {
    "Nombre": "Majesty: The Fantasy Kingdom Sim",
    "Género": "Estrategia en tiempo real",
    "Desarrollador": "Cyberlore Studios",
    "Clasificación ESRB": "T (Teen)"
  },
  {
    "Nombre": "Perfect Dark",
    "Género": "Shooter en primera persona",
    "Desarrollador": "Rare",
    "Clasificación ESRB": "M (Mature)"
  },
  {
    "Nombre": "Deus Ex",
    "Género": "RPG / Shooter",
    "Desarrollador": "Ion Storm",
    "Clasificación ESRB": "M (Mature)"
  },
  {
    "Nombre": "Chrono Cross",
    "Género": "JRPG",
    "Desarrollador": "Square",
    "Clasificación ESRB": "T (Teen)"
  },
  {
    "Nombre": "Hitman: Codename 47",
    "Género": "Acción / Sigilo",
    "Desarrollador": "IO Interactive",
    "Clasificación ESRB": "M (Mature)"
  }
] """

def save_videogames_to_csv(file_path):
    videogames = []
    headers = ["Nombre", "Género", "Desarrollador", "Clasificación ESRB"]

    total_videogames = int(input("¿Cuántos videojuegos desea ingresar?: "))

    for i in range(total_videogames):
        print(f"Ingrese los detalles del videojuego {i + 1}:")
        nombre = input("Nombre: ")
        genero = input("Género: ")
        desarrollador = input("Desarrollador: ")
        clasificacion = input("Clasificación ESRB: ")

        videogame = {
            "Nombre": nombre,
            "Género": genero,
            "Desarrollador": desarrollador,
            "Clasificación ESRB": clasificacion
        }
        videogames.append(videogame)
        print()  # Línea en blanco entre entradas

    with open(file_path, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(videogames)

if __name__ == "__main__":
    save_videogames_to_csv('videogames.csv')