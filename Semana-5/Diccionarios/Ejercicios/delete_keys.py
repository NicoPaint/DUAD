list_of_keys = ["access_level", "age"]
employee = {
    "name": "John", 
    "email": "john@ecorp.com", 
    "access_level": 5, 
    "age": 28
}

for key in list_of_keys:
    if(employee.get(key)):
        employee.pop(key)

print(employee)