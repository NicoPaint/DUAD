employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

results = {}

for employee in employees:
    if(results.get(employee.get("department"))):
        results[employee.get("department")].append(employee.get("name"))
    else:
        results[employee.get("department")] = [employee.get("name")]


print(results)