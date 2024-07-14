"""Generator Expression

This module demonstrates the use of generator expressions in Python.

An issue with list comprehension is that for larger lists, it consumes a lot of
memory. This is because it creates the entire list in memory before returning
it. Also can be time consuming because it has to iterate over the entire list
before returning the result.

Generator expressions are a more memory efficient way to create lists. They
return a generator object, which is an iterator that generates the items on the
fly. This means that the entire list is not stored in memory, and the items are
generated as needed.
"""


def fibb_example():
    """Generator Example: Fibbonacci series

    The generator will begin its execution till it reaches the yield statement.
    It will then return the value and pause the execution.

    When the `next()` function is called, the execution will resume from the point
    where it was paused. This will continue till the generator is exhausted.

    The generator will raise a `StopIteration` exception when it is exhausted, just
    like any other iterator."""

    def fibonacci_lc(count):
        """List comprehension for fibonacci series

        The list comprehension will return the entire list of fibonacci series.
        """
        a, b = 0, 1
        return [b := a + (a := b) for _ in range(count)]

    def fibonacci_gc():
        """Generator for fibonacci series

        The generator will yield the next number in the series. The series will
        begin with 1 and 1. The next number will be the sum of the previous two
        numbers.
        """
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    count = 100

    # The loop will wait for the entire list to be generated before printing it
    fib_lc = fibonacci_lc(count)
    for i in range(count):
        print(fib_lc[i], end=", ")

    # The generator will generate the next number in the series on the fly
    fib_gc = fibonacci_gc()
    for _ in range(count):
        print(next(fib_gc), end=", ")


def gen_exp_example():
    """Generator Expression Example

    The generator expression is similar to list comprehension, but it returns a
    generator object instead of a list. The generator object is an iterator that
    generates the items on the fly, which means that the entire list is not stored
    in memory.
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # List comprehension
    squares_lc = [num**2 for num in nums]
    print(squares_lc)

    # Generator expression
    squares_ge = (num**2 for num in nums)
    for square in squares_ge:
        print(square, end=", ")


if __name__ == "__main__":
    fibb_example()
    gen_exp_example()
