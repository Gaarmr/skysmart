num = 7007

a=num//1000

b=num//100
b=b%10

c=num%100
c=c//10

d=num%10

a=str(a*a)
b=str(b*b)
c=str(c*c)
d=str(d*d)

print(a+b+c+d)