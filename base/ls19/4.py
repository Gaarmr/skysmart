def temp_to_f(t):
    temp_f = int(t[:-1]) * (9/5) + 32
    print(temp_f, 'f', sep='')

def temp_to_c(t):
    temp_c = (int(t[:-1]) - 32) * (5/9)
    print(temp_c, 'c', sep='')

def set_temp():
    t = input('Введите температуру в формате #c - для цельсия и #f - для фаренгейта ')
    if t[-1] == 'c':
        temp_to_f(t)
    elif t[-1] == 'f':
        temp_to_c(t)
    else:
        print('Не ввели букву. #c - для цельсия и #f - для фаренгейта ')

set_temp()