def print_all_pairs(my_dict):
    for key1 in my_dict: # O(n) -> n = len(my_dict.keys())
        for key2 in my_dict: # O(n^2) -> n = len(my_dict.keys())
            print(f"{key1}-{key2}") # O(1)


""" 
- Preguntas:
    - ¿Cuál es la complejidad temporal?: Esta va a ser O(n^2) donde n es igual a la cantidad de claves que tenga el diccionario
    - ¿Cuanto dura si hay `1` millón de claves?: Va a durar 1 millon^2, es decir, 1 billon de operaciones.
"""