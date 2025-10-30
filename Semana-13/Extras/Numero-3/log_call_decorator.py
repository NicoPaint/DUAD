from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"func: {func.__name__} - args: {', '.join(map(str, args))} - [{datetime.now()}] - Resultado: {func(*args)}")

        return func(*args, **kwargs)
    
    return wrapper