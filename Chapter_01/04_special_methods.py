"""Special Methods

This module contains the application of special methods for the `SerialNumber` and `Series` classes.

Especially, the `__format__` method is used to format the serial number as a three-digit number.
"""


class SerialNumber:
    """A class to represent a serial number."""

    def __init__(self, value):
        """Initialize the serial number.

        The serial number is a three-digit number.

        Args:
            `value` (`int`): The value of the serial number.

        Raises:
            `ValueError`: If the value is not an integer."""
        if type(value) != int:
            raise ValueError("Value must be an integer")
        self._value = value

    def __format__(self, format_spec):
        return f"{self._value:{format_spec}}"

    def __str__(self):
        return format(f"{self._value:03}")

    def __repr__(self):
        return f"SerialNumber({self._value})"


class Series:
    """A class to represent a series of serial numbers."""

    def __init__(self, count):
        """Initialize the series of serial numbers.

        The series will contain `count` serial numbers.

        Args:
            `count` (`int`): The number of serial numbers in the series.
        """
        self._count = count
        self._numbers = [SerialNumber(i) for i in range(1, count + 1)]

    def __getitem__(self, index):
        return self._numbers[index]

    def __len__(self):
        return len(self._numbers)

    def __iter__(self):
        return iter(self._numbers)

    def __reversed__(self):
        return reversed(self._numbers)

    def __contains__(self, value):
        return value in self._numbers

    def __str__(self):
        return str(list(map(str, self._numbers)))

    def __repr__(self):
        return f"Series({self._count:!r})"

    def __bool__(self):
        return bool(self._numbers)


if __name__ == "__main__":
    series = Series(5)

    print(series)
    # Output: ['001', '002', '003', '004', '005']
