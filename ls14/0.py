a = 0

for temp in range(5):
    print(a)
    a += 1
    if a == 3:
        a += 2
    if a == 4:
        a += 3
    if a == 5:
        a += 4
    else: 
        a += 1
    
print(a)