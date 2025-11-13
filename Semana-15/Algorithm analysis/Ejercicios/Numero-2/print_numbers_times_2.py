def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n) -> n = len(numbers_list)
		print(number * 2) # O(1)

# Por lo que print_numbers_times_2 es O(n)