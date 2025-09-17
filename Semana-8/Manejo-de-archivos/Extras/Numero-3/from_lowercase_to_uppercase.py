def convert_to_uppercase(path1, path2):
    uppercase_list = []

    with open(path1) as file:
        for line in file:
            uppercase_list.append(line.upper())
    
    with open(path2, "w") as file:
        for line in uppercase_list:
            file.writelines(line)


if __name__ == "__main__":
    convert_to_uppercase("lowercase.txt", "uppercase.txt")