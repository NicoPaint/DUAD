def sum_all_numbers(number_list):

    if not isinstance(number_list, list):
        raise TypeError("El argumento debe ser una lista de números")

    total = 0
    for number in number_list:
        total += number
    
    return total

print(sum_all_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))