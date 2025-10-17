def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Todos los argumentos deben ser numéricos")
            
        return func(*args)
        
    return wrapper