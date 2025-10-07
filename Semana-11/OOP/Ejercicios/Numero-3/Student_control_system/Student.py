class Student:
    def __init__(self, name, section, spanish_grade, english_grade, socials_grade, science_grade, average):
        self.name = name
        self.section = section
        self.grades = {
            "Español": spanish_grade,
            "Ingles": english_grade,
            "Sociales": socials_grade,
            "Ciencias": science_grade
        }
        self.average = average
    

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