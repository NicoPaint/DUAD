variable_global = "Mocca"

def my_function():
    global variable_global
    local_variable = "Miwi"
    print(f"Esta es la variable global antes de cambiarla: {variable_global}")
    variable_global = "pici"
    print(f"Esta es la variable global despues de cambiarla: {variable_global}")

my_function()
print(local_variable)