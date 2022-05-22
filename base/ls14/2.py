n = 3
x = 3

i = 1
fac = 1

res=1

while i<=n:
    y = x ** i
    fac *= i 
    res += y / fac
    i += 1
    print(res, y, fac, i)


# from math import factorial

# def e(x, n):
#     return sum(x**i / factorial(i) for i in range(n + 1))