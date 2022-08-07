a = '90134865793180467'
b = ''
for i in a:
    if i.isdigit():
        i = int(i)
        if i > 4:
            b += '1'
        else:
            b += '0'
print(b)
