def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = ['булка', 3.14, [5, True]]
print_params(*values_list)

print_params(b = 25)

print_params(c = [1,2,3])

values_dict = {'a':15, 'b':'norma', 'c':[5, 8, 111]}
print_params(**values_dict)
