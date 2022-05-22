# s = "qrpvcure zr"

# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)

# print("".join([d.get(c, c) for c in s]))  

# sbbone


n = input('Введите строку ')
abc = "abcdefghijklmnopqrstuvwxyz"
k = 13
a = []

for i in n:
    a.append(abc[(abc.find(i)+k)%26])

print(a)