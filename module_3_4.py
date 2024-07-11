def single_root_words(k, *args):
    same_words = []
    for i in args:
        li = i.lower()
        lk = k.lower()
        if ((li in lk) or (lk in li)):
            same_words.append(i)
        else:
            continue
    return same_words

other_words = ['rich', 'richiest', 'orichalcum', 'cheers', 'richies']
#other_words = ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel']
#other_words = ['дом', 'домашний', 'шалаш', 'домовой', 'дом', ' кошка']
print(single_root_words(*other_words))
