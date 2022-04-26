slovo = str(input())
a = slovo[::-1] # [::-1] [начало строки:конец строки:шаг-1] -1 означает в обратном порядке
print(a)
if slovo == a:
    print("yes")
else:
    print("no")