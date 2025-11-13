def just_numbers(func):
    def wrapper(num_list):
        for item in num_list:
            if not isinstance(item, (int, float, range)):
                raise ValueError("La lista contiene elementos no numéricos")
        
        return func(num_list)
    
    return wrapper