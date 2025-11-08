from bubble_sort import bubble_sort

def validate_all_are_numbers(num_list):
    for item in num_list:
        if not isinstance(item, (int, float, range)):
            raise ValueError("La lista contiene elementos no numéricos")
    
    return bubble_sort(num_list)


if __name__ == "__main__":
    my_num_list_1 = [1, 7, 3, 2, 9, 9 ,6 , -8]
    my_num_list_2 = [1, "7", 3, 2, "string", 9 ,6 , -8]

    try:
        validate_all_are_numbers(my_num_list_1)
        print(my_num_list_1)
        validate_all_are_numbers(my_num_list_2)
        print(my_num_list_2)
    except ValueError as error:
        print(f"Error: {error}")