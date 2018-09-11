import timeit
import functools


def calc_values(x, y: int):
    return x * y


numbers = [2, 3, 5, 8, 13]

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
# print(sum(numbers))

result = 1
for x in numbers:
    result *= x
print(result)

result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)








