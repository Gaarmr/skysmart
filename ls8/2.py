a = 100
b = 100
c = 100
d = 1

if a != b and a != c and a != d:
    print(a)
elif b != a and b != c and b != d:
    print(b)
elif c != a and c != b and c != d:
    print(c)
elif d != a and d != c and d != b:
    print(d)
else:
    print('Все равны')