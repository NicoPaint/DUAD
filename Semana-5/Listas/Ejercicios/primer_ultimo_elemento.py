my_list = [4, 3, 6, 1, 7]

primer = my_list[0]
ultimo = my_list[len(my_list) - 1]

my_list[0] = ultimo
my_list[len(my_list) - 1] = primer

print(my_list)