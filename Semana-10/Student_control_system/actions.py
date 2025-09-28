def do_we_continue(phrase_to_show):
    user_response = input(f"\n¿{phrase_to_show}? (Y/N): ").strip().upper()

    while user_response not in ["Y", "N"]:
        user_response = input(f"La opción que ingresaste no es valida, ¿{phrase_to_show}? (Y/N): ").strip().upper()
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


def format_name(name):
    formated_name = ""
    word = ""

    for index, letter in enumerate(name):
        word += letter
        if letter in [" ", "-"]:
            formated_name += word.capitalize()
            word = ""
        elif index == len(name) - 1:
            formated_name += word.capitalize()
    
    return formated_name


def is_valid_name(name):
    is_a_valid_name = False

    while not is_a_valid_name:
        did_it_break = False

        for letter in name:
            if letter in [" ", "-"]:
                continue
            elif letter.isdigit() or not letter.isalnum():
                did_it_break = True
                break
        
        if did_it_break or name == "":
            name = input("La opción que ingresaste no es valida, Ingrese un nombre que no tenga números, caracteres especiales o que no este vácio: ").strip()
        else:
            is_a_valid_name = True
    
    return format_name(name)


def is_valid_section(section):
    while True:
        if len(section) > 3:
            section = input("La opción que ingresaste no es valida, Ingrese una sección entre 1 a 12 y A a F: ").strip().upper()
            continue
        else:
            number = ""
            letter = ""
            for character in section:
                if character.isdigit():
                    number += character
                elif character.isalpha:
                    letter += character
                else:
                    section = input("La opción que ingresaste no es valida, Ingrese una sección entre 1 a 12 y A a F: ").strip().upper()
                    continue

            if number == "":
                number = "0"
            
            if int(number) > 12 or int(number) < 1:
                section = input("La opción que ingresaste no es valida, Ingrese una sección entre 1 a 12 y A a F: ").strip().upper()
                continue

            if letter not in ["A", "B", "C", "D", "E", "F"]:
                section = input("La opción que ingresaste no es valida, Ingrese una sección entre 1 a 12 y A a F: ").strip().upper()
                continue
        
            return section


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


def student_exists(name, section, students):
    is_duplicated = False

    for student in students:
        if student["Nombre"] == name and student["Sección"] == section:
            print("El estudiante que ingresasté ya existe en la lista (no pueden haber estudiantes duplicados). Por favor intentalo nuevamente: \n")
            is_duplicated = True
            return is_duplicated
    
    return is_duplicated


def review_student_information_submitted(student):
    is_information_correct = True

    print("\nPor favor revisa la información que acabas de ingresar: \n")
    for key, values in student.items():
        if key == "Promedio":
            continue

        print(f"{key}: {values}")
    
    user_response = do_we_continue("Es la informacion del estudiante correcta")
    if user_response == "N":
        is_information_correct = False

    return is_information_correct


def is_students_list_empty(students):
    if not students:
        print("No hay información de los estudiantes aún. Por favor ingresala o importala desde el menú principal")
        return True
    else:
        return False


def enter_students_info(students):
    more_students = True
    counter = 1

    print("-" * 70)
    while more_students:
        print(f"Por favor ingrese la información del estudiante número {counter}:")
        student_name = is_valid_name(input("Nombre completo: ").strip())
        student_section = is_valid_section(input("Sección: ").strip().upper())

        if student_exists(student_name, student_section, students):
            continue

        spanish_grade = is_valid_grade(input("Nota de Español: ").strip())
        english_grade = is_valid_grade(input("Nota de Ingles: ").strip())
        socials_grade = is_valid_grade(input("Nota de Sociales: ").strip())
        science_grade = is_valid_grade(input("Nota de Ciencias: ").strip())
        student_avg = calculate_average([spanish_grade, english_grade, socials_grade, science_grade])

        student = {
            "Nombre": student_name,
            "Sección": student_section,
            "Notas": {
                "Español": spanish_grade,
                "Ingles": english_grade,
                "Sociales": socials_grade,
                "Ciencias": science_grade
            },
            "Promedio": student_avg
        }

        if not review_student_information_submitted(student):
            continue

        students.append(student)
        counter += 1

        other_student = do_we_continue("Desea continuar agregando estudiantes")
        if other_student == "N":
            more_students = False

    print(students)
    return students


def view_all_students_info(students):

    if is_students_list_empty(students):
        return

    print("-" * 70)
    print("Aqui esta la informacion de todos los estudiantes:\n")
    print(f"Estudiantes totales: {len(students)}\n")
    print("-" * 25)

    for index, student in enumerate(students):
        print(f"Estudiante número {index + 1}")
        for key, value in student.items():
            if key == "Notas":
                print(f"{key}: ")
                for subject, grade in student[key].items():
                    print(f"\t{subject}: {grade}")
            else:
                print(f"{key}: {value}")
        print("-" * 25)
        print()


def sorted_by_average(student):
    return student["Promedio"]


def view_top_3_students_info(students):

    if is_students_list_empty(students):
        return

    if len(students) >= 3:
        message = "de los 3 mejores estudiantes"
    elif len(students) == 2:
        message = "de los 2 mejores estudiantes"
    else:
        message = "del mejor estudiante"

    print("-" * 70)
    print(f"Aqui esta la informacion {message}:\n")
    print("-" * 25)

    sorted_students = students.copy()
    sorted_students.sort(key = sorted_by_average, reverse = True)

    for index, student in enumerate(sorted_students):
        if index == 3:
            break
        print(f"Estudiante número {index + 1}")
        for key, value in student.items():
            if key == "Notas":
                print(f"{key}: ")
                for subject, grade in student[key].items():
                    print(f"\t{subject}: {grade}")
            else:
                print(f"{key}: {value}")
        print("-" * 25)
        print()


def view_students_avg_grade(students):
    
    if is_students_list_empty(students):
        return
    
    students_average_list = [student["Promedio"] for student in students]
    overall_average = round(calculate_average(students_average_list), 2)

    print("-" * 70)
    print()
    print(f"El promedio general de todos los estudiantes es: {overall_average}")
    print()
    print("-" * 70)



def delete_student(students):
    print("Eliminar estudiante")
    return students


def view_failed_students(students):
    print("Ver estudiantes reprobados")