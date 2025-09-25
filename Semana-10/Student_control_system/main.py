from menu import menu_student_control_system
import actions
import data

def start_student_control_system():
    students = []

    print("Bienvenido al sistema de control de estudiantes\n")
    user_action = menu_student_control_system()

    while int(user_action) in range(1, 9):
        match user_action:
            case "1":
                students = actions.enter_students_info(students)
            case "2":
                actions.view_all_students_info(students)
            case "3":
                actions.view_top_3_students_info(students)
            case "4":
                actions.view_students_avg_grade(students)
            case "5":
                data.export_students_data("test", students)
            case "6":
                students = data.import_students_data("test")
            case "7":
                students = actions.delete_student(students)
            case "8":
                actions.view_failed_students(students)

        other_action = actions.do_we_continue("Desea continuar con otra acción")
        if other_action == "N":
            break

        user_action = menu_student_control_system()
    
    print("Gracias por su tiempo, nos vemos una próxima vez")

if __name__ == "__main__":
    try:
        start_student_control_system()
    except Exception as error:
        print(error)