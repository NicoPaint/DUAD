def generate_list_trios(list_a, list_b, list_c):
	result_list = [] # O(1)
	for element_a in list_a: # O(n) -> n = len(list_a)
		for element_b in list_b: # O(n * m) -> n = len(list_a) & m = len(list_b)
			for element_c in list_c: # O(n * m * p) -> n = len(list_a), m = len(list_b) & p = len(list_c)
				result_list.append(f'{element_a} {element_b} {element_c}') # O(1)
				
	return result_list # O(1)


# Por lo que generate_list_trios es O(n * m * p), donde si n = m = p esta se convertiría en O(n^3)