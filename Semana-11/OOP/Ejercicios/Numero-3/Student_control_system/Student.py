class Student:
    def __init__(self, student_info):
        self.name = student_info["Nombre"]
        self.section = student_info["Sección"]
        self.grades = student_info["Notas"]
        self.average = student_info["Promedio"]
    

    def __str__(self):
        return f"""
        Nombre: {self.name}
        Sección: {self.section}
        Notas: 
            Español: {self.grades["Español"]}
            Ingles: {self.grades["Ingles"]}
            Sociales: {self.grades["Sociales"]}
            Ciencias: {self.grades["Ciencias"]}
        Promedio: {self.average}
        """
    
    def show_failed_subjects(self):
        print(f"Nombre: {self.name}")
        print(f"Sección: {self.section}")
        print("Materias reprobadas:")
        for subject, grade in self.grades.items():
            if grade < 60:
                print(f"\t{subject}: {grade}")