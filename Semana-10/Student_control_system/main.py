from menu import menu_student_control_system
import actions
import data

def start_student_control_system():
    print("Bienvenido al sistema de control de estudiantes\n")
    user_action = menu_student_control_system()

    print(user_action)

if __name__ == "__main__":
    try:
        start_student_control_system()
    except Exception as error:
        print(error)