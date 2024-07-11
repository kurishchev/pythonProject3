def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list_2 = ['булка', 3.14 ]
print_params(*values_list_2, 57)