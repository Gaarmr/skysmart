b=[]
n=int(input('Введите длинну списка '))

for i in range(n):
    b.append(int(input()))

print(b)

# maxn=b[0]
# for i in b:
#     if i>maxn:
#         maxn=i

# print(maxn)


print(max(b))