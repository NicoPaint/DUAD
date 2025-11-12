def bubble_sort(num_list):

    for outer_index in range(0, len(num_list) - 1): # O(n) -> n = len(num_list) - 1
        did_they_change = False # O(1)

        for inner_index in range(0, len(num_list) - 1 - outer_index): # O((n^2) -> n = len(num_list) - 1
            current_num = num_list[inner_index] # O(1)
            next_num = num_list[inner_index + 1] # O(1)

            if current_num > next_num: # O(1)
                did_they_change = True # O(1)
                num_list[inner_index] = next_num # O(1)
                num_list[inner_index + 1] = current_num # O(1)

        if not did_they_change: # O(1)
            break # O(1)
    
    return num_list # O(1)


# Por lo que bubble_sort es O(n^2).
