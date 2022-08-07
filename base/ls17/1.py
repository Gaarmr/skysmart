# n = input('Введите целое число ')
# fl=0

# for i in range(len(n) - 1):
#     if abs(int(n[i]) - int(n[i+1])) == 1:
#         fl=1
#     else:
#         fl=0
#         break

# print(fl)


n = input()
ln = len(n)
for i in range(ln-1):
    if abs(int(n[i]) - int(n[i+1])) == 1:
        pass
    else:
        print(0)
        break
else:
    print(1)
