from menu import menu_student_control_system
import actions
import data

def start_student_control_system():
    print("Bienvenido al sistema de control de estudiantes\n")
    user_action = menu_student_control_system()

    while int(user_action) in range(1, 9):
        match user_action:
            case "1":
                actions.enter_students_info()
            case "2":
                actions.view_all_students_info()
            case "3":
                actions.view_top_3_students_info()
            case "4":
                actions.view_students_avg_grade()
            case "5":
                data.export_students_data("test")
            case "6":
                data.import_students_data("test")
            case "7":
                actions.delete_student("Pedro", "11A")
            case "8":
                actions.view_failed_students()

        do_we_continue = input("¿Desea continuar con otra acción? (Y/N): ").strip().upper()

        while do_we_continue not in ["Y", "N"]:
            do_we_continue = input("La opción que ingresaste no es valida, ¿Desea continuar con otra acción? (Y/N): ").strip().upper()

        if do_we_continue == "N":
            break

        user_action = menu_student_control_system()
    
    print("Gracias por su tiempo, nos vemos una proxima vez")

if __name__ == "__main__":
    try:
        start_student_control_system()
    except Exception as error:
        print(error)