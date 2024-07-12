def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        first = 1
    if len(str_number) == 1:
        x = first
    else:
        x = first * get_multiplied_digits(int(str_number[1:]))
    return x


h = int(input('Введите целое число: '))
if h == 0:
    print('Произведение цифр равно: 0')
else:
    print('Произведение цифр равно: ', get_multiplied_digits(h))
