#Version 1
def manual_add(number):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n) -> n = number
        result += i # O(1)
    return result # O(1)

# manual_add es O(n).

#Version 2
def add_formula(number):
    return number * (number + 1) // 2 # O(1)

# add_formula es O(1).

# si number = 1 000 000 000, yo usaría la version 2. Ya que al ser O(1) se va a demorar lo mismo sin importar el tamaño de number.