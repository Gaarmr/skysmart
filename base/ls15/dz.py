b = []
summ = 0
n = int(input('Введите длинну списка '))

for i in range(n):
    b.append(int(input()))
    summ += b[i]

print(summ/n)
