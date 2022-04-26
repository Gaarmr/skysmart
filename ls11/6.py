n = 7
sum_of_factorials = 1
curr_factorial = 1

for i in range(2, n+1):
    curr_factorial *= i
    if i % 2 == 0:
        sum_of_factorials -= curr_factorial
    else:
        sum_of_factorials += curr_factorial

print(curr_factorial, sum_of_factorials)