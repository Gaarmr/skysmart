n = '105501'
digits = []
# digits = [int(c) for c in n]

for i in n:
    digits.append(int(i))

length = len(digits)
middle = length // 2
offset = length % 2

if sum(digits[:middle]) == sum(digits[middle+offset:]):
    print(1)
else:
    print(0)


# print(int(sum(digits[:middle]) == sum(digits[middle+offset:])))


# def sum_of_digits(num):
#     return sum(map(int, str(num)))

# if (sum_of_digits(num_str[:mid_idx]) == sum_of_digits(num_str[mid_idx + len(num_str) % 2:])):
#     print(1)
# else:
#     print(0)
