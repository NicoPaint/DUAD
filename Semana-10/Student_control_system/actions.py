def do_we_continue(phrase_to_show):
    user_response = input(f"\n¿Desea continuar {phrase_to_show}? (Y/N): ").strip().upper()

    while user_response not in ["Y", "N"]:
        user_response = input(f"La opción que ingresaste no es valida, ¿Desea continuar {phrase_to_show}? (Y/N): ").strip().upper()
    print()
    
    return user_response


def calculate_average(notes_list):
    if not notes_list:
        return 0
    return sum(notes_list)/len(notes_list)


def is_a_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_valid_name(name):
    print("valid name")


def is_valid_section(section):
    print("Valid section")


def is_valid_grade(str_number):
    while True:
        if is_a_float(str_number):
            number = float(str_number)
            if number not in range(0, 101):
                str_number = input("La opción que ingresaste no es valida, Ingrese un número del 0 al 100: ")
                continue
            else:
                return number
        else:
            str_number = input("La opción que ingresaste no es valida, Ingrese un número del 0 al 100: ")
            continue


def student_exists(name, section):
    print("Exist")

def enter_students_info(students):
    more_students = True
    counter = 1

    while more_students:
        print(f"Por favor ingrese la información del estudiante número {counter}:")
        student_name = input("Nombre completo: ").strip()
        student_section = input("Sección: ").strip()
        spanish_grade = is_valid_grade(input("Nota de Español: ").strip())
        english_grade = is_valid_grade(input("Nota de Ingles: ").strip())
        socials_grade = is_valid_grade(input("Nota de Sociales: ").strip())
        science_grade = is_valid_grade(input("Nota de Ciencias: ").strip())
        student_avg = calculate_average([spanish_grade, english_grade, socials_grade, science_grade])

        student = {
            "name": student_name,
            "section": student_section,
            "grades": {
                "Spanish": spanish_grade,
                "English": english_grade,
                "Socials": socials_grade,
                "Sciences": science_grade
            },
            "average": student_avg
        }

        students.append(student)
        counter += 1

        other_student = do_we_continue("agregando estudiantes")
        if other_student == "N":
            more_students = False

    print(students)
    return students


def view_all_students_info(students):
    print("Ver información de todos los estudiantes")


def view_top_3_students_info(students):
    print("Ver información de los 3 mejores estudiantes")


def view_students_avg_grade(students):
    print("Ver nota promedio de todos los estudiantes")


def delete_student(students):
    print("Eliminar estudiante")
    return students


def view_failed_students(students):
    print("Ver estudiantes reprobados")