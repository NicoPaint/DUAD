def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    
    return wrapper

@repeat_twice
def print_hello_name(name):
    print(f"Hello, {name}")


print_hello_name("Natasha")
print_hello_name("Josh")
print_hello_name("Amelia")