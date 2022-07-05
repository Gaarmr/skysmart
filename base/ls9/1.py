a = 4
b = 5
c = 6

if (a+b>c and a+c>b and b+c>a) and c**2 == a**2 + b**2:
    print(1)
elif (a+b>c and a+c>b and b+c>a) and b**2 == a**2 + c**2:
    print(1)
elif (a+b>c and a+c>b and b+c>a) and a**2 == b**2 + c**2:
    print(1)
else:
    print(0)