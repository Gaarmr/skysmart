fib1 = 0
fib2 = 1
 
n = 233

fib_sum = 1 

while fib_sum<=n:
    print(fib_sum, end=' ')
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum


    


