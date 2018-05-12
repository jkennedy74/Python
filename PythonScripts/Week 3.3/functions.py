# -*- coding: UTF-8 -*-
"""Functions."""


# Basic Definition
def name(parameters):
    """Function Docstring."""
    # code goes here
    return


# Simple Example with no parameters
def foo():
    """Don't forget the docstring!"""
    print("Bar")


# Simple Example with one parameter
def show(message):
    """Display a message."""
    print(message)

# Remember that an argument is the value that you pass to the function parameter
# In this case, "Hello, World!" is the argument and message is the parameter
show("Hello, World!")


# Example using positional arguments
def make_quesadilla(protein, topping):
    """Make a Quesadilla."""
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)

# Supply the arguments (values) when calling the function
make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")

# @NOTE: Order is important when supplying arguments!
make_quesadilla("sour cream", "beef")


# We can specify default values for parameters
def make_quesadilla(protein, topping="sour cream"):
    """Make a Quesadilla."""
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)

# Make a quesadilla using the default topping
make_quesadilla("chicken")

# Make a quesadilla with a new topping
make_quesadilla("beef", "guacamole")


# Example of returning a value
def square(number):
    """Square the number."""
    return number * number

print(square(2))
print(square(3))


# You can pass any object to a function.
def sum(numbers):
    """Sums all numbers in a list."""
    sum = 0
    for number in numbers:
        sum += number
    return sum

# We can pass a list of numbers to the function.
print(sum([1, 2, 3, 4, 5]))
print(sum(range(5)))
data = [1, 1, 2, 2]
print(sum(data))


# Functions can return multiple values
def min_max(numbers):
    """Finds the min and max value in a list of numbers."""
    return min(numbers), max(numbers)

# @NOTE: A tuple of both values are returned
both = min_max([1, 2, 3])
print(both)

# We can "Unpack" the return into separate variables
min_number, max_number = min_max([1, 2, 3])
print(min_number)
print(max_number)


# Arguments can also be optional if we specify a default value for the parameter
def sort_numbers(numbers, reverse=False):
    """Sorts a list of numbers.

    Args:
        numbers (list): A list of numbers to sort.
        reverse (bool): A boolean value to determine the sort order.

    Returns:
        list: A sorted list of integers.
    """
    sorted_numbers = numbers[:]
    return sorted(sorted_numbers, reverse=reverse)


sorted_numbers = sort_numbers([1, 3, 5, 7])
sorted_numbers = sort_numbers([1, 3, 5, 7], reverse=True)
sorted_numbers = sort_numbers([1, 3, 5, 7], True)

# Docstrings are accessed with __doc__ attribute
print(sort_numbers.__doc__)

# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    sort_numbers([1, 3, 5, 7])
