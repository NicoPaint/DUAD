first_name = input("ingrese su nombre: ")
last_name = input("ingrese su apellido: ")
age = int(input("ingrese su apellido: "))

if(age < 2):
    print("Es un bebé")
elif(age >= 2 and age < 11):
    print("Es un niño")
elif(age >= 11 and age < 13):
    print("Es un preadolecente")
elif(age >= 13 and age < 18):
    print("Es un adolecente")
elif(age >= 18 and age < 30):
    print("Es un adulto joven")
elif(age >= 30 and age < 65):
    print("Es un adulto")
elif(age >= 65):
    print("Es un adulto mayor")
