n = 10
sum_of_factorials = 0
curr_factorial = 1

for i in range(1, n+1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial

    print(curr_factorial, sum_of_factorials)