a1 = ['Привет', 'я', 'изучаю', 'Python']

a2 = ['Привет', 'Довольно сложная задача', 'Python — популярный язык программирования']
a3 = []


for s in a1:
    for x in a2:
        if s in x:
            a3.append(s)
            break


print(a3)


# result = [s for s in a1 if any(s in x for x in a2)]