# Version 1
def linear_search(my_list, target):
    for item in my_list: # O(n) -> n = len(my_list)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)


# Version 2
def binary_search(my_list, target):
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(Log n) -> n = len(my_list). Esto sucede porque con cada iteracion la lista se divide en la mitad. Es decir que las veces que se ejecuta el ciclo va a ser igual a las veces que se pueda dividir n en 2 hasta llegar a 1, o log n.
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else:
            high = mid - 1 # O(1)
    return False

""" 
Preguntas:
- ¿Cuál es la complejidad de cada algoritmo?: 
    La busqueda lineal es O(n) donde n es len(my_list).
    La búsqueda binaria es O(Log n) donde n es len(my_list).
- ¿En qué condiciones conviene usar cada uno?:
    Esta busqueda binaria conviene usarla cuando los valores de la lista estan ordenadas ascendentemente, ya que se demora menos con la misma cantidad de datos que la lineal. 
    En cambio si la lista esta desordenada, conviene usar la búsqueda lineal.
- ¿Qué pasa si la lista no está ordenada?:
    Si la lista no esta ordenada y se usa la búsqueda binaria, es poco probable de hayar el valor objetivo.

"""