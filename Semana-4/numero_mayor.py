first = int(input("Ingrese su primer número: "))
second = int(input("Ingrese su segundo número: "))
third = int(input("Ingrese su tercero número: "))

higher = first

if(higher < second):
    higher = second
    
if(higher < third):
    higher = third

print(f"El número mayor es {higher}")