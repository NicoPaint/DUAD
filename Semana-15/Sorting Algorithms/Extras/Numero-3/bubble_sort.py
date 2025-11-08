from number_validator_2 import just_numbers

def bubble_sort(num_list):

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


@just_numbers
def bubble_sort_decorated(num_list):

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


if __name__ == "__main__":
    my_num_list_1 = [1, 7, 3, 2, 9, 9 ,6 , -8]
    my_num_list_2 = [1, "7", 3, 2, "string", 9 ,6 , -8]

    try:
        bubble_sort_decorated(my_num_list_1)
        print(my_num_list_1)
        bubble_sort_decorated(my_num_list_2)
        print(my_num_list_2)
    except ValueError as error:
        print(f"Error: {error}")