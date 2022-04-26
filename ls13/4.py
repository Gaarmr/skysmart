n = 17
 
if n < 2:
    print("Число должно быть больше 1")
    quit()
elif n == 2:
    print("Это простое число")
    quit()
 
i = 2 # первый делитель
 
limit = n**(1/2)
 
while i <= limit:
    if n % i == 0:
        print("Это сложное число")
        quit() # выход из программы
    i += 1 # переход к следующему делителю
 
print("Это простое число")