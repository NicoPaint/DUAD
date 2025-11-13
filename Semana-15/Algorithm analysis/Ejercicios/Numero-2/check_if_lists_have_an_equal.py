def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: # O(n) -> n = len(list_a)
		for element_b in list_b: # O(n * m) -> n = len(list_a) & m = len(list_b)
			if element_a == element_b: # O(1)
				return True # O(1)
				
	return False # O(1)


# Por lo que check_if_lists_have_an_equal es O(n * m). donde si n = m se convertiría a O(n^2)