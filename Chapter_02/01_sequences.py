"""Sequences: Classification on the basis of C implementation

This module demonstrates the classification of sequences based on the C implementation.

The python standard library provides two types of sequences:
Container and Flat sequences:

- Container sequences hold references to the objects they contain, which may be of 
any type. Examples include `list`, `tuple`, `collections.deque`

- Flat sequences physically store the value of each item within its own memory space, 
and not as distinct objects. Examples include `str`, `bytes`, `array.array`

Every python object in memory has a header with metadata about the object, including
a reference count, object type, and object value. For example, a float object has a
`ob_refcnt`, `ob_type`, and `ob_fval`.

The reference count is the number of references to the object including variable 
references, function arguments, and container references. When the reference count
reaches zero, the memory is deallocated.

The `sys.getrefcount()` function returns the reference count of an object. The count
is higher than expected because the function itself holds a reference to the object.
"""

import array
import sys


def sequence_type_example():
    """This function demonstrates the classification of sequences based on C implementation.

    We will compare the addresses of the objects in a container sequence and a flat sequence.
    """

    def print_addresses(sequence):
        """Print the address of each item in the sequence"""
        for item in sequence:
            print(f"Address of {item}: {hex(id(item))}")

    # Container sequence
    # We can store different types of objects in a container sequence
    container = [1, "cat", 3.14, [1, 4]]

    print("Container sequence: Scattered addresses")
    print_addresses(container)

    # Flat sequence
    # We can only store objects of the same type in a flat sequence
    # `i` is the type code for signed integers, `d` for double precision floats
    # `b` for bytes, `u` for unicode characters etc.
    flat = array.array("i", [1, 2, 3, 4, 5])

    print("\nFlat sequence: Contiguous addresses")
    print_addresses(flat)

    # Reference count
    print("\nReference count of container sequence")
    print(sys.getrefcount(container))
    # Output: 2
    # The reference count is 2 because the function call itself holds a reference to the object
    # and the container sequence holds a reference to the object. The function calls that have been
    # completed are not included in the count. Therefore, the reference made by passing it to the
    # `print_addresses` is not included in the count.


if __name__ == "__main__":
    sequence_type_example()
