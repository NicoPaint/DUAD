import csv

def show_csv_content(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Leer la primera fila como encabezados
        for row in reader:
            for header, value in zip(headers, row): # Emparejar encabezados con valores
                print(f"{header}: {value}")
            
            print() # Línea en blanco entre registros


if __name__ == "__main__":
    show_csv_content('../../Ejercicios/Numero-1/videogames.csv')