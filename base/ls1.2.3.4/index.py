a = 'Привет, я изучаю Python'
b = 'P'
ind1 = a.index(b)
ind2 = a.index(b) + len(b)

print(f'a[{ind1}:{ind2}]')
