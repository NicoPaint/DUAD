import csv
import os
import ast
import actions
from Student import Student

def validate_csv_file_name(action):
    while True:
        has_extension = False
        file_name = input(f"Por favor ingrese solo el nombre del archivo csv que desea {action}, no agregue ninguna extensión: ").strip()
        for letter in file_name:
            if letter in [".", "/"]:
                print("Nombre invalido. Por favor intentelo nuevamente")
                has_extension = True
                break
        if has_extension:
            continue

        break

    return file_name


def choose_write_action(phrase_to_show):
    user_choice = input(f"\n{phrase_to_show}. Por favor seleccione la acción que desea hacer:\n" \
    "\n" \
    "1. Sobreescribirlo.\n" \
    "2. Anexar la información al final.\n" \
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
    students_list = []
    for student in students_data:
        students_list.append(student.export_student_attributes_as_a_dictionary())

    file_name = validate_csv_file_name("exportar")
    file_path = f"./files/{file_name}.csv"

    if os.path.exists(file_path):
        user_action_confirmation = choose_write_action("El archivo ya existe")
        if user_action_confirmation == "1":
            print(f"Sobreescribiendo archivo {file_name}.csv ...")
            with open(file_path, mode="w", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                writer.writerows(students_list)
        else:
            print(f"Anexando información al archivo {file_name}.csv ...")
            with open(file_path, mode="a", encoding="utf-8") as file:
                writer = csv.DictWriter(file, headers)
                writer.writerows(students_list)
    else:
        print(f"Creando archivo {file_name}.csv ...")
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(students_list)
    
    print(f"La información de los estudiantes ha sido exportada con exito al archivo {file_name}.csv en la ruta {file_path}")

    
    return actions.empty_students_list(students_data)


def import_students_data(students_data):
    file_name = validate_csv_file_name("importar")
    file_path = f"./files/{file_name}.csv"

    if os.path.exists(file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            preview_students_data = []
            for student in reader:
                for key in student.keys():
                    if key == "Notas":
                        student_grades_dict = ast.literal_eval(student[key])
                        student[key] = student_grades_dict
                    elif key == "Promedio":
                        student_avg_float = float(student[key])
                        student[key] = student_avg_float
                 
                student_obj = Student(student)
                preview_students_data.append(student_obj)

            if preview_students_data:
                if not students_data:
                    students_data = preview_students_data.copy()
                    print("\n¡Importación realizada con exito!")
                else:
                    user_confirmation = choose_write_action("Parece que ya tienes información de algunos estudiantes agregadas al sistema")
                    if user_confirmation == "1":
                        students_data = preview_students_data.copy()
                    else:
                        for student in preview_students_data:
                            students_data.append(student)
                    print("\n¡Importación realizada con exito!")
            else:
                print("El archivo que importaste esta vacio")
    else:
        print(f"El archivo {file_name}.csv no existe en la ruta {file_path}. Por favor asegurate que el nombre que ingresaste coincida exactamente con el nombre del archivo")

    return students_data