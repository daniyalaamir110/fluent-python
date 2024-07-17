"""Match Case Pattern

Pattern matching is a feature that allows you to match a value against a pattern.
The `match` statement is used to match a value against patterns. The patterns are
defined using the `case` statement, which are checked in order. 

The patterns can be simple values, sequences, or types. We can also have a guard
clause that is an additional condition that must be satisfied for the pattern to
match.

In STL, these types are compatible with sequence patterns:
`list`, `tuple`, `range`, `array.array`, `collections.deque`, `memoryview`
"""

import math
from pprint import pprint
import sys


def arithmetic_operations_example():
    """Arithmetic operations using pattern matching."""

    def handle_command(command):
        match command:
            case ["add", a, b]:
                return a + b
            case ["add", *nums]:
                return sum(nums)
            case ["sub", a, b]:
                return a - b
            case ["mul", a, b]:
                return a * b
            case ["mul", *nums]:
                return math.prod(nums)
            case ["div", a, b]:
                return a / b

    operation = sys.argv[1]
    nums = tuple(map(int, sys.argv[2:]))

    result = handle_command([operation, *nums])

    print(result)


def manipulating_data_entries_example():
    """Manipulating data entries using pattern matching.

    The list contains the following types of data entries:

    - Integer: Multiply the number by 2.
    - String: Reverse the string.
    - List of integers: Calculate the sum of the integers.
    - Tuple with first element as a string and second as an integer: Repeat the
      string by the integer value.
    - Dictionary with keys as strings and values as integers: Create a new
      dictionary with the same keys but values incremented by 1.
    - Any other type: Return the entry as is.
    """

    def handle_data_entry(entry):
        match entry:
            case int(num):
                return num * 2
            case str(text):
                return "".join(reversed(text))
            case [*nums] if all(isinstance(num, int) for num in nums):
                return sum(nums)
            case (str(text), int(count)):
                return text * count
            case dict(data) if all(
                isinstance(key, str) and isinstance(value, int)
                for key, value in data.items()
            ):
                return {key: value + 1 for key, value in data.items()}
            case _:
                return entry

    data_entries = [
        42,
        "hello",
        [1, 2, 3],
        ("repeat", 3),
        {"key1": 1, "key2": 2},
        100,
        "world",
        [4, 5, 6],
        ("python", 2),
        {"a": 10, "b": 20},
    ]

    results = list(map(handle_data_entry, data_entries))

    pprint(results)
    # [84,
    #  'olleh',
    #  6,
    #  'repeatrepeatrepeat',
    #  {'key1': 2, 'key2': 3},
    #  200,
    #  'dlrow',
    #  15,
    #  'pythonpython',
    #  {'a': 11, 'b': 21}]


if __name__ == "__main__":
    # arithmetic_operations_example()
    manipulating_data_entries_example()
