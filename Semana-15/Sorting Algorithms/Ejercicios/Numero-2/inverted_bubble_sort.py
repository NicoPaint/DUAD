def inverted_bubble_sort(num_list):

    for outer_index in range(0, len(num_list) - 1):
        did_they_change = False

        for inner_index in range(len(num_list) - 1, 0 + outer_index, -1):
            current_num = num_list[inner_index]
            previous_num = num_list[inner_index - 1]

            if current_num < previous_num:
                did_they_change = True
                num_list[inner_index] = previous_num
                num_list[inner_index - 1] = current_num

        if not did_they_change:
            break
    
    return num_list

my_list = [5, 3, 6, -9, 0, 1]
my_sorted_list = inverted_bubble_sort(my_list)
print(my_sorted_list)
my_list = [1, 3, 5, 7, 9]
my_sorted_list = inverted_bubble_sort(my_list)
print(my_sorted_list)
my_list = [1, 3, 5, -7, 9]
my_sorted_list = inverted_bubble_sort(my_list)
print(my_sorted_list)