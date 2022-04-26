# сколько трёхзначных чисел можно составить из 4 цифр
a='9156'

for i in range(0, len(a)):
    for j in range(0, len(a)):
        for k in range(0, len(a)):
            if( a[i] != a[k] ) and (a[i] != a[j]) and (a[j] != a[k]):
                print(a[i],a[j],a[k])