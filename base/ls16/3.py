n = int(input('Введите длинну списка '))
a = [input() for i in range(n)]

# for i in range(n):
#     a.append(int(input()))

print(a)

counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
