a = 999

x = a // 100
y = a % 100
y = y // 10
z = a % 10

print(x, y, z)

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print(3)
elif (x % 2 == 0 and y % 2 == 0) or (y % 2 == 0 and z % 2 == 0) or (x % 2 == 0 and z % 2 == 0):
    print(2)
elif x%2 == 0 or y%2 == 0 or z%2 == 0:
    print(1)
else:
    print(0)
