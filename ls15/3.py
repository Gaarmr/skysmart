b=[]
summ=0
for i in range(4):
    b.append(int(input()))
    summ+=b[i]

s=sum(b)

print(s)
print(summ/4)