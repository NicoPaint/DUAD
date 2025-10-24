def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Todos los argumentos deben ser numéricos")
        for values in kwargs.values():
            if not isinstance(values, (int, float)):
                raise ValueError("Todos los argumentos deben ser numéricos") 

        return func(*args, **kwargs)
        
    return wrapper