def calculate_average(notes_list):
    if not notes_list:
        return 0
    return sum(notes_list)/len(notes_list)

def enter_students_info():
    print("Ingresar informaciónn estudiante")


def view_all_students_info():
    print("Ver información de todos los estudiantes")


def view_top_3_students_info():
    print("Ver información de los 3 mejores estudiantes")


def view_students_avg_grade():
    print("Ver nota promedio de todos los estudiantes")


def delete_student(name, classroom):
    print("Eliminar estudiante")


def view_failed_students():
    print("Ver estudiantes reprobados")