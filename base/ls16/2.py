b=[]
n=int(input('Введите длинну списка '))

for i in range(n):
    b.append(int(input()))

print(b)

minn=max(b)
for i in b:
    if i%2!=0 and i<minn:
        minn=i

if minn%2==0:
    print(0)
else:
    print(minn)