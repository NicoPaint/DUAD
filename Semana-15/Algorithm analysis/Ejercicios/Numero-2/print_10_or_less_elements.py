def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) # O(1)
	for index in range(min(list_len, 10)): # O(n) -> n = 10, es decir, O(10)
		print(list_to_print[index]) # O(1)


#Por lo que print_10_or_less_elements es O(n), donde sabemos que el maximo valor del ciclo va a ser 10, lo que nos daría que es O(10)