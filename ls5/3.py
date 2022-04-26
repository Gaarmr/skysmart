a = 1
b = 1
c = 1

if a < 0:
    if b < 0:
        if c < 0:
            print(3)
        else:
            print(2)
    else:
        if c < 0:
            print(2)
        else:
            print(1)
else:
    if b < 0:
        if c < 0:
            print(2)
        else:
            print(1)
    else:
        if c < 0:
            print(1)
        else:
            print(0)

