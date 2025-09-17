def find_prime_numbers(number_list):
    prime_number_list = []

    for number in number_list:
        is_prime = True

        for evaluator in range(2, number):
            if(number%evaluator == 0):
                is_prime = False
                break
        
        if(is_prime):
            prime_number_list.append(number)


    return prime_number_list


print(find_prime_numbers([1, 4, 6, 7, 13, 9, 67, 20, 2, 19, 88]))