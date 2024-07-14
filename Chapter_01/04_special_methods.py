class SerialNumber:
    def __init__(self, value):
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
    def __init__(self, count):
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


def main():
    series = Series(5)

    print(series)
    # Output: ['001', '002', '003', '004', '005']


if __name__ == "__main__":
    main()
