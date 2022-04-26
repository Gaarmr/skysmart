def temp_c():
    temp_c = int(input('введите температуру по цельсию '))
    temp_f = temp_c * (9/5) + 32
    print(temp_f)

def temp_f():
    temp_f = int(input('введите температуру по фаренгейту '))
    temp_c = (temp_f - 32) * (5/9)
    print(temp_c)



def set_temp():
    n = int(input('Выбери температуру 1 - цельсий. 2 - фаренгейт '))
    if n == 1:
        temp_c()
    else:
        temp_f()


set_temp()