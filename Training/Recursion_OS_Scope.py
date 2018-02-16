def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

# for i in range(10):
#     print(i, fact(i))
#     print(i, factorial(i))

# Fibonacci
for i in range(36):
    # print(i, fib(i)) # Recursively is taking more time for Fibonacci.
    print(i, fibonacci(i)) # Faster method.

#########################
# Files and Directories #
#########################
import os

def list_directories(s):

    def dir_list(d):  # Nested function, defined within a function.
        nonlocal tab_stop  # State that it belongs to the outer scope. It has to exist.
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")

list_directories('.')

####
print()
listing = os.walk('.')
for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)

###################################
# def spam1():

#     def spam2():

#         def spam3():
#             z = " even"
#             z += y
#             print("In spam3, locals are {}".format(locals()))
#             return z

#         y = " more " + x  # y must exist before spam3 is called
#         y += spam3()  # do not combine these assignments.
#         print("In spam2, locals are {}".format(locals()))
#         return y

#     x = "spam"  # x must exist before spam2 is called
#     x += spam2()  # do not combine these assignments
#     print("In spam1, locals are {}".format(locals()))
#     return x

# print(spam1())
# print(locals())
# print(globals())
