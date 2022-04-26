a = 1
b = 2 
c = 3 
if not a == b == c:
    a, b, c = c, a, b
    print(a,b,c)
if a == b:
    a, b = c, a
elif  a == c:
    a, c = b, a
else:
    print(a + c)