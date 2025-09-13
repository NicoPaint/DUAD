def print_first():
    print("Esta es la primera función")


def print_second():
    print_first()
    print("Esta es la segunda función que llama a la primera")


print_second()