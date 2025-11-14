def bubble_sort(num_list):

    if not isinstance(num_list, list):
        raise TypeError("El parametro debe ser una lista")

    for outer_index in range(0, len(num_list) - 1):
        did_they_change = False

        for inner_index in range(0, len(num_list) - 1 - outer_index):
            current_num = num_list[inner_index]
            next_num = num_list[inner_index + 1]

            if current_num > next_num:
                did_they_change = True
                num_list[inner_index] = next_num
                num_list[inner_index + 1] = current_num

        if not did_they_change:
            break
    
    return num_list

my_list = [8, 5, 2, 7, 8, 4 ,9]
my_list.sort()
print(my_list)