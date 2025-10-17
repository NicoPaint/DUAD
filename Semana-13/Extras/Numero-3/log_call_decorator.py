from datetime import datetime

def log_call(func):
    def wrapper(*args):
        print(f"func: {func.__name__} - args: {', '.join(map(str, args))} - [{datetime.now()}] - Resultado: {func(*args)}")

        return func(*args)
    
    return wrapper