calls = 0

def count_calls():
    global calls
    calls += 1
    return calls



def string_info(string1):
    k = count_calls()
    x = string1
    kort = (len(x), x.upper(), x.lower())
    return kort


def is_contains(string1, list_to_search):
    k = count_calls()
    x = False

    for i in range(len(list_to_search)):
        y = str(list_to_search[i])
        if y.lower() == string1.lower():
            x = True
            break
        else:
            continue
    return x


a ='kljdfgJlknY244'
d = ['d', 'g', 1, 'd', 'kljdfgJlknY244']
s_i = string_info(a)
print(s_i)
i_c = is_contains(a, d)
print(i_c)
print('Количество вызовов= ', calls)





