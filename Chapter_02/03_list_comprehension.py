"""List Comprehension

This module demonstrates the use of list comprehension in Python.

It is a technique to create lists in a concise way. Using the traditional
approach, you would need to write a loop to create a list. With LC, we can
do that in a single line, which looks more explicit, and readable.

List comprehension cannot fully replace loops because we use loops for
several purposes, like aggregation and other tasks, whereas LC has a more
explicit intent i.e. creating list from an iterable.
"""


def symbols_example():
    """Symbols Example

    This function demonstrates the use of list comprehension to get the ASCII
    codes of the symbols in a string.
    """

    def get_codes_without_lc(string):
        """Get the ASCII codes of the symbols in the string

        This function uses a loop to get the ASCII codes of the symbols in the
        string and append to a list, initialized as empty.
        """
        codes = []
        for symbol in string:
            codes.append(ord(symbol))

        return codes

    def get_codes_with_lc(string):
        """Get the ASCII codes of the symbols in the string

        This function uses list comprehension to get the ASCII codes of the
        symbols in the string.
        """
        return [ord(symbol) for symbol in string]

    def get_codes_with_map(string):
        """Get the ASCII codes of the symbols in the string

        This function uses the `map()` function to get the ASCII codes of the
        symbols in the string.
        """
        return list(map(ord, string))

    symbols = "@#$%^&*"

    codes_wo_lc = get_codes_without_lc(symbols)
    print(codes_wo_lc)

    codes_lc = get_codes_with_lc(symbols)
    print(codes_lc)

    codes_map = get_codes_with_map(symbols)
    print(codes_map)


def even_number_example():
    """Even Number Example

    This function demonstrates the use of list comprehension to get the even
    """

    def get_evens_without_lc(nums):
        """Get the even numbers from the list

        This function uses a loop to get the even numbers from the list and
        append to a list, initialized as empty.
        """
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)

        return evens

    def get_evens_with_lc(nums):
        """Get the even numbers from the list

        This function uses list comprehension to get the even numbers from the
        list.
        """
        return [num for num in nums if num % 2 == 0]

    def get_evens_with_filter(nums):
        """Get the even numbers from the list

        This function uses the `filter()` function to get the even numbers from
        the list.
        """
        return list(filter(lambda x: x % 2 == 0, nums))

    # We can also appy filters to the list comprehension
    nums = [1, 4, 2, 5, 6, 8, 10]

    # Get even numbers
    evens = [last := num for num in nums if num % 2 == 0]

    # Another method
    evens = list(filter(lambda x: x % 2 == 0, nums))

    print(evens)

    # Warlus operator `:=`
    # This operator assigns a value to a variable as part of an expression.

    # This would raise `NameError`
    # print(num)

    # This would not raise an error
    print(last)


if __name__ == "__main__":
    symbols_example()
    even_number_example()
