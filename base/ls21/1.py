def temp_to_f(t):
    temp_f = t * (9/5) + 32
    print(temp_f, 'f', sep='')


def temp_to_c(t):
    temp_c = (t - 32) * (5/9)
    print(temp_c, 'c', sep='')


def set_temp(t, scale):
    if scale == 'c':
        temp_to_f(t)
    elif scale == 'f':
        temp_to_c(t)
    else:
        print('Аргументы функции температура и шкала ')


set_temp(-1914, 'c')
