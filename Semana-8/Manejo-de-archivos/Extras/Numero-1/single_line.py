def create_single_line_file(path1, path2):
    word_list = ""
    file_length = 0

    with open(path1) as file:
        file_length = len(file.readlines())

    with open(path1) as file:
        for index, word in enumerate(file.readlines()):
            new_word = ""
            for letter in word:
                if (letter == "\n"):
                    break
                new_word += letter

            if (index == file_length - 1):
                word_list += new_word
                break

            word_list += f"{new_word} "
    
    with open(path2, "w") as file:
        file.write(word_list)


if __name__ == "__main__":
    create_single_line_file("multiple_lines.txt", "single_line.txt")