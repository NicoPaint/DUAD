def menu_student_control_system():
    
    user_choice = input("Por favor seleccione la acción que desea hacer:\n" \
    "\n" \
    "1. Ingresar información de los estudiantes uno por uno.\n" \
    "2. Ver la información de todos los estudiantes.\n" \
    "3. Ver el top 3 de los estudiantes con el mejor promedio.\n" \
    "4. Ver la nota promedio de todos los estudiantes\n" \
    "5. Exportar todos los datos actuales a un CSV.\n" \
    "6. Importar todos los datos de un CSV previamente guardado.\n" \
    "7. Eliminar a un estudiante.\n" \
    "8. Eliminar a todos los estudiantes.\n" \
    "9. Mostrar estudiantes reprobados.\n" \
    "10. Salir de programa.\n" \
    "\n" \
    "Por favor escribe el número de la acción: ").strip()
    print()

    while user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        user_choice = input("La opción que ingresaste no es valida, por favor vuelve a ingresarla: ").strip()

    return user_choice