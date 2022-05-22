a = 'qweqweqwe1'

if len(a) >= 8 and not a.isupper() and not a.islower() and not a.isalpha() and not a.isdigit():
    print('Hard')
elif len(a) >= 8 and a.islower() and not a.isalpha():
    print('Medium')
elif len(a) >= 8 and (a.isalpha() or a.isdigit()):
    print('Easy')
else:
    print('Very easy')
