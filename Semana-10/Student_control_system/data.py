import csv
import os
import actions

def validate_csv_file_name(action):
    while True:
        has_extension = False
        file_name = input(f"Por favor ingrese solo el nombre del archivo csv que desea {action}, no agregue ninguna extensión: ")
        for letter in file_name:
            if letter in [".", "/"]:
                print("Nombre invalido. Por favor intentelo nuevamente")
                has_extension = True
                break
        if has_extension:
            continue

        break

    return file_name


def choose_write_action():
    user_choice = input("\nEl archivo ya existe. Por favor seleccione la acción que desea hacer:\n" \
    "\n" \
    "1. Sobreescribirlo.\n" \
    "2. Anexar la información al final del archivo.\n" \
    "\n" \
    "Por favor escriba el número de la acción: ").strip()
    print()

    while user_choice not in ['1', '2']:
        user_choice = input("La opción que ingresaste no es valida, por favor vuelve a ingresarla: ").strip()

    return user_choice


def export_students_data(students_data):
    if actions.is_students_list_empty(students_data):
        return None
    
    actions.view_all_students_info(students_data)
    user_continue_confirmation = actions.do_we_continue("Desea continuar con la exportación")
    if user_continue_confirmation == "N":
        print("Exportación cancelada")
        return None

    headers = ["Nombre", "Sección", "Notas", "Promedio"]
    file_name = validate_csv_file_name("exportar")
    file_path = f"./files/{file_name}.csv"

    if os.path.exists(file_path):
        user_action_confirmation = choose_write_action()
        if user_action_confirmation == "1":
            print(f"Sobreescribiendo archivo {file_name}.csv ...")
            with open(file_path, mode="w", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                writer.writerows(students_data)
        else:
            print(f"Anexando información al archivo {file_name}.csv ...")
            with open(file_path, mode="a", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writerows(students_data)
    else:
        print(f"Creando archivo {file_name}.csv ...")
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(students_data)
    
    print(f"La información de los estudiantes ha sido exportada con exito al archivo {file_name}.csv en la ruta {file_path}")


def import_students_data():
    """ file_name = validate_csv_file_name("importar")
        
    file_path = f"./files/{file_name}.csv"
 """
    students_data = []
    return students_data