import math


def get_sum(*nums: int):
    sum = 0

    for n in nums:
        sum += n

    print("Sum: ", sum)

get_sum(-1, 0, math.inf)