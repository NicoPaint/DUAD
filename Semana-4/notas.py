grades = []
done = False

while(not done):
    grades.append(int(input("Por favor ingrese la nota: ")))
    if(input("¿Terminó de ingresar sus notas? (s/n): ") == "s"):
        done = True

grades_approved = 0
sum_approved = 0

grades_failed = 0
sum_failed = 0

sum_grades = 0


for grade in grades:
    if(grade >= 70):
        sum_approved += grade
        grades_approved +=1
    elif(grade < 70):
        sum_failed += grade
        grades_failed += 1
    
    sum_grades += grade

total_avg = sum_grades / len(grades)

if(grades_approved > 0):
    approved_avg = sum_approved / grades_approved
else:
    approved_avg = "N/A"

if(grades_failed > 0):
    failed_avg = sum_failed / grades_failed
else:
    failed_avg = "N/A"

print(
f"""
    Aprobaste {grades_approved} de {len(grades)}
    Reprobaste {grades_failed} de {len(grades)}
    Tu promedio final fue: {total_avg}
    Tu promedio de las aprobadas fue: {approved_avg}
    Tu promedio de las reprobadas fue: {failed_avg}
""")