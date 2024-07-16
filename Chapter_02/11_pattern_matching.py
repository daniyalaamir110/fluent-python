import math
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


if __name__ == "__main__":
    arithmetic_operations_example()
