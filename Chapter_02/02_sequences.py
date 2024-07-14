"""Sequences: Classification on the basis of mutability

This module demonstrates the classification of sequences based on mutability.

There are two types of sequences based on mutability:
- Mutable sequences can be modified after creation. They implement
the `collections.abc.MutableSequence` abstract base class.
Examples include `list`, `bytearray`, `array.array`

- Immutable sequences cannot be modified after creation. They
implement the `collections.abc.Sequence` abstract base class.
Examples include `str`, `bytes`, `tuple`
"""

from collections import abc

if __name__ == "__main__":

    print("List is a mutable sequence")
    print(issubclass(list, abc.MutableSequence))

    print("\nTuple is an immutable sequence")
    print(issubclass(tuple, abc.Sequence))

    my_list = [1, 2, 3, 4, 5]

    # Mutable sequences can be modified
    my_list[0] = 10  # __setitem__()

    del my_list[1]  # __delitem__()

    my_list.insert(2, 20)  # insert()

    my_list.append(6)  # append()

    my_list.reverse()  # reverse()

    my_list.remove(3)  # remove()

    popped = my_list.pop(3)  # pop()

    # my_list.extend([7, 8, 9]) # extend()

    # We prefer the `+=` operator over the + operator for extending a list
    # because the `+=` operator modifies the list in place, while the + operator
    # creates a new list and assigns it to the variable. `+=` corresponds to the
    # `__iadd__()` method.
    # my_list = my_list + [7, 8, 9]
    my_list += [7, 8, 9]

    print(my_list)
