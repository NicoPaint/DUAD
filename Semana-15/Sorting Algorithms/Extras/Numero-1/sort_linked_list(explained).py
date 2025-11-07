""" Este archivo es para hacer la explicación de como llegué a la solución de este algoritmo (ascendant bubble sort function para la estructura de datos Linkedlist). Ya que necesitó esfuerzo mental para obtener cada uno de los bloques de código """

""" Primero se agregó una propiedad dinamica a la Linkedlist llamada length (revisar archivo Linkedlist.py para su referencia) para poder calcular cuantos elementos existen en la lista y asi poder hacer el recorrido de ellos de manera mas facil en la función de ordenamiento"""
from LinkedList import Linkedlist

def sort_linked_list(linked_list):
    """ Este es el primer ciclo de la Bubble sort function. va de cero a la longitud de la lista menos uno, ya que se trabaja con dos elementos por cada interación (un elemento y su elemento siguiente) por lo que no se necesita llegar hasta el ultimo elemento por indice"""
    for outer_index in range(0, linked_list.length - 1):
        """ Esta variable se usa para verificar que hubo al menos un cambio en cada iteración para determinar si la lista ya esta ordenada o no, asi parar la ejecución si es necesario. Es la primera optimización de este tipo de algoritmo de organización """
        did_they_change = False

        """ Primero vamos a evaluar los 2 primeros elementos de la lista. Como el único punto de entrada es el head, creamos 2 variables, una que referencee al head y otra al siguiente elemento del head """
        current_node = linked_list.head
        next_node = current_node.next

        """ Ahora evaluamos si el valor del head es mayor que el del siguiente elemento para intercambiarlos de puesto si es necesario"""
        if current_node.data > next_node.data:
            """ Si si es mayor, significa que el segundo elemento debe convertirse en el nuevo head de la lista y se debe reasignar el apuntador respectivamente. 
            
            Este es el proceso que se lleva acabo:
                    1.  Conectamos el actual head con en el tercer elemento de la lista a través de su atrubuto next. Asi desconectamos el segundo de la lista para acomodarlo en el primer lugar.
                    2. Posicionamos el segundo elemento en la primera posición, haciendo que su atributo next apunte ahora actual head. Ahora todos los elementos estan conectados.
                    3. Cambiamos el apuntador Head hacia el nuevo primer elemento de la lista. Al hacer esto, pasamos el punto de entrada de la lista a ese elemento y podemos recorrer toda la lista con ese cambio de orden hecho
                    4. Debemos seguir con el resto de la lista por lo que debemos referenciar correctamente los elementos de ella con las variables current_node y next_node respectivamente. Al mirar como quedaron esas variables en los pasos anteriores nos damos cuenta que current_node ahora referencea al elemento #2 de la lista (Que es el siguiente elemento que debemos evaluar en la itearación) por lo que no debemos hacer nada respecto a ella, ya que está referenciando al elemento correcto, y next_node ahora referencea al primer elemento de la lista. Por lo que cambiamos esa variable para que ahora referencee al tercer elemento de la lista y asi empezar con el segundo ciclo del bubble sort function.
            """
            linked_list.head.next = next_node.next
            next_node.next = linked_list.head
            linked_list.head = next_node
            next_node = current_node.next
        else:
            """ Si no es mayor, significa que no debemos hacer ningún cambio, por lo que debemos cambiar la referencia de las variables para evaluar las siguientes posiciones. Por lo que reasignamos a current_node para que referencee ahora al segundo elemento de la lista y next_node al tercero de ella, y asi empezar con el segundo ciclo del bubble sort function."""
            current_node = linked_list.head.next
            next_node = current_node.next

        """ Para el segundo ciclo del bubble sort function, decidí hacerlo con un contador y asi poder controlar hasta cuando se ejecuta el ciclo while. 
        
        Como en el if-else anterior ya evaluamos las primeras 2 posiciones, el contador empieza en 1 y no en 0 """
        counter = 1

        """ En este ciclo se implementa la segunda optimización del bubble sort para solo evaluar los movimientos necesarios de los elementos. Es por eso que se resta el indece del ciclo exterior, porque con cada iteración de este ya se debío haber ordanado un elemento. """
        while counter < (linked_list.length - 1 - outer_index):
            
            """ Esto solo es un print para poder visualizar cuantas iteracione hubo y que elementos se evaluaron """
            print(f'-- Iteracion {outer_index}, {counter}. Elemento actual: {current_node.data}, Siguiente elemento: {next_node.data}')

            """ Ahora evaluamos si el valor del current_node es mayor que el del siguiente para intercambiarlos de puesto si es necesario  """
            if current_node.data > next_node.data:
                """ Si si es mayor, debemos hacer el cambio de posición de los elementos

                Este es el proceso que se lleva acabo:
                    1. Desconectamos al next_node de la lista para poder asignarlo antes que el current_node. Eso se logra haciendo que el next del current_node apunte ahora a el next del next_node.
                    2. Ahora posicionamos el next_node como el elemento anterior al current_node. Eso se logra haciendo que el next del next_node apunte hacia el current_node.
                    3. Ahora el problema es que next_node no esta conectada a la lista en general. Si la recorrieramos, la función no imprimiria el next_node. Por lo que para poder conectarla, debemos capturar de cierta manera al node anterior al current_node. Para eso creamos una nueva variable llamada previous_node que inicialmente va a apuntar al head (nuestro punto de entrada a la lista).
                    4. Ahora debemos capturar ese nodo anterior con previous_node. Por lo que recorremos la lista a traves de un while hasta que el nodo siguiente del previous node sea igual al current_node.
                    5. Ya con el nodo correcto referenciado, ahora conectamos next_node a la lista haciendo que el next de previous_node apunte al next_node. Y como el next de next_node ya apuntaba al current_node, la lista esta unida y con ese tramo ordenado.
                    6. Finalmente debemos asegurarnos que las variables de referencia current_node y next_node este apuntando a los elementos correctos para la siguiente iteración. Al mirar como quedaron esas variables en los pasos anteriores nos damos cuenta que current_node ahora referencea al elemento en la posición siguiente a evaluar en la lista por lo que no debemos hacer nada respecto a ella, ya que está referenciando al elemento correcto, y next_node ahora referencea al elemento que acabamos de organizar de la lista. Por lo que cambiamos esa variable para que ahora referencee al siguiente elemento del siguiente elemento a organizar en la lista
                    7. Como si hubo un cambio, pasamos la variable de la primera optimización para que siga con el siguiente ciclo
                """
                current_node.next = next_node.next
                next_node.next = current_node
                previus_node = linked_list.head
                while previus_node.next != current_node:
                    previus_node = previus_node.next
                
                previus_node.next = next_node
                next_node = current_node.next
                did_they_change = True
            else:

                """ Si no es mayor, simplemente reasignamos current_node y next_node al siguiente para de elementos a evaluar en la lista """
                current_node = next_node
                next_node = current_node.next

            """ Finalizado cada iteración del ciclo interno, sumamos 1 al contador para poder salir del ciclo cuando se terminen los elementos """
            counter += 1

        """ Esta es la segunda parte de la primera optimización de este algoritmo. Si al finalizar cualquier ciclo while no hubo cambios, significa que la lista ya esta ordenada y no es necesario seguir recorriendola por lo que rompe el ciclo externo y termina la ejecución de esta función """
        if not did_they_change:
            break


my_linked_list = Linkedlist()
my_linked_list.insert_back(37)
my_linked_list.insert_back(3)
my_linked_list.insert_back(33)
my_linked_list.insert_back(30)

my_linked_list.print_all()
sort_linked_list(my_linked_list)
print()
my_linked_list.print_all()