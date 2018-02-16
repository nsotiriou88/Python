def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """  # Docstring for the function "factorial".
    if n <= 1:
        return 1
    else:
        # print(n/0)
        return n * factorial(n-1)

try:
    print(factorial(1000))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")
# except (RecursionError, OverflowError, ZeroDivisionError):
except ZeroDivisionError:
    print("What are you doing dividing by zero???")

print("Program terminating")

##########################
import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:  # The order of the exceptions matters.
        # except:  # For general usage as a wildcard for exceptions.
            sys.exit(1)
        except ValueError:
            print("Invalid number entered, please try again")
        finally:  # Useful for closing connections, databases etc. It is always executed at after all others.
            print("The finally clause always executes!")

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)  # Use coding/numbers for debugging.
else:
    print("Division performed successfully")
