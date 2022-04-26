def temp_f():
    temp_f = int(input('введите температуру по фаренгейту '))
    temp_c = (temp_f - 32) * (5/9)
    print(temp_c)

temp_f()