import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start  # Implementation of a generator.
        start += 1

# _ = input("line 12")
# big_range = range(10000)
big_range = my_range(5)  # Assigning a generator to a value.
# _ = input("line 15")

print(next(big_range)) # This allows the generator to proceed one step.
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

# _ = input("line 22")
for val in big_range:
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again... or not")
# for i in big_range:  # This one is not running, as the generator has no more values to extract.
for i in my_range(5):
    print("i is {}".format(i))

# coco = range(1000)  # This is class: 'range'.
print()

####### Fibonacci #######
def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

for i in range(0,21):
    print(next(fib), end=' ')
# print(next(fib))
# print(next(fib))

print()

####### Pi #######
def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


# Creating an Infinate Series!!!
def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))
