a = '908065033'
b = ''
for i in a:
    if i.isdigit() == True:
        i = int(i)
        if i > 4:
            b += '1'
        else:
            b += '0'
print(b)
