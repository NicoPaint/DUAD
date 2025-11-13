def bubble_sort(num_list):
    iterations = 0
    exchanges = 0

    for outer_index in range(0, len(num_list) - 1):
        did_they_change = False

        for inner_index in range(0, len(num_list) - 1 - outer_index):
            current_num = num_list[inner_index]
            next_num = num_list[inner_index + 1]

            if current_num > next_num:
                did_they_change = True
                exchanges += 1
                num_list[inner_index] = next_num
                num_list[inner_index + 1] = current_num

            iterations += 1
        if not did_they_change:
            break
    
    return {
        "sorted list": num_list,
        "iterations": iterations,
        "exchanges": exchanges
    }

my_list = [5, 3, 6, -9, 0, 1]
my_sorted_dict = bubble_sort(my_list)
print(f"Lista ordenada: {my_sorted_dict["sorted list"]}")
print(f"Iteraciones: {my_sorted_dict["iterations"]}")
print(f"Intercambios: {my_sorted_dict["exchanges"]}")