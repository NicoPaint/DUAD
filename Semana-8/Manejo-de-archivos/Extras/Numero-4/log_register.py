def register_the_log(path):
    user_log = input("Ingrese su mensaje a guardar: ")

    with open(path, "a") as file:
        file.writelines(f"{user_log}\n")


if __name__ == "__main__":
    register_the_log("user_log.txt")