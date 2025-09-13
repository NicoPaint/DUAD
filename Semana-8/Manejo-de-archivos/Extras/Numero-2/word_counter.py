def count_file_words(path):
    counter = 0
    with open(path) as file:
        for line in file:

            if (line == "\n"):
                continue

            word = ""
            for index, letter in enumerate(line):
                if (index == 0 and letter == " "):
                    continue
                elif (letter == " " or letter == "\n"):
                    counter += 1
                    word = ""
                    continue
                elif (letter == "." or letter == "," or letter == "(" or letter == ")"):
                    continue

                word += letter
            
            if (word != ""):
                counter += 1
    
    print(f"El archivo {path} contiene {counter} palabras")

    return counter


if __name__ == "__main__":
    count_file_words("paragraph.txt")