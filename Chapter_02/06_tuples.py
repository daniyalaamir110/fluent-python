"""Tuple

This module demonstrates the use of tuples in Python.

A tuple is a collection which is ordered and immutable. In Python tuples are written with round brackets.
Tuples can be used as records, and as immutable lists.

- Tuple as a record: Tuples are used to group related pieces of information. For example, a tuple can be 
used to represent a person's profile. Sorting a tuple makes no sense, as the order of the elements is
important, as specific positions denote a different field. In this case, the tuple can be used as a record.

- Tuple as an immutable list: Tuples can be used as an immutable list. For example, a tuple can be used to
represent a fibonacci series. The order of the elements is important, but the elements themselves are not
related to a specific field. In this case, the tuple can be used as an immutable list. Immutable means that 
the reference to the tuple cannot be changed, but the elements themselves can be mutable. For example, a tuple
can contain a list, and the list can be modified, since list is a mutable sequence.

Unpacking a tuple: Unpacking a tuple assigns each element of the tuple to a variable. The number of variables
should match the number of elements in the tuple, otherwise an error will be raised. If we want to ignore
some elements, we can use an underscore `_` to represent the ignored elements. If we want to separate the
first element from the rest of the elements, we can use the `*` operator, to pack the rest of the elements
into a list.

Comparing tuples: Tuples can be compared using the comparison operators. The comparison is done element-wise.

Tuples being immutable will ensure that the references to its elements are not changed. However, if there is
a mutable object in the tuple, the object can be modified without changing the reference to the tuple, in which
case the tuple will be considered as changed indirectly. Therefore, tuples with mutable objects are a source of 
bugs, and we recommend using immutable objects in tuples.
"""


def tuples_as_records_example():
    """Tuples as records example

    This function demonstrates the use of tuples as records. A tuple is used to represent a person's profile.
    We unpack the tuple to get the individual elements, and print them.
    """
    profile = ("John Doe", (1990, 1, 1), "M", 70.5, ("New York", "USA"))

    # Unpacking the tuple
    # We use _ to ignore the weight
    # The number of variables should match the number of elements in the tuple
    name, dob, gender, _, location = profile

    print("Name: %s" % name)
    print("Date of Birth: %s-%s-%s" % dob)
    print("Gender: %s" % gender)
    print("Location: %s, %s" % location)


def tuple_comparison_example():
    """Tuple comparison example

    This function demonstrates the comparison of tuples. We compare two tuples element-wise. We use a mutable
    object in the tuple to demonstrate that the tuple will be considered as changed indirectly, even though the
    references to the elements are not changed.
    """
    tp_1 = (1, 2, [3, 4])
    tp_2 = (1, 2, [3, 4])

    print(tp_1 == tp_2)  # True

    tp_1[-1].append(5)

    print(tp_1 == tp_2)  # False

    # Better to use immutable objects in tuples
    # tp_3 = (1, 2, (3, 4))


def hashable_tuple_example():
    """Hashable tuple example

    This function demonstrates that a tuple is hashable if all its contents can never change. If a tuple contains
    a list, it is not hashable, because the list can be modified. If a tuple contains another tuple, it is hashable,
    because the tuple is immutable.

    A hashable object is an object that can be used as a key in a dictionary or as an element in a set. A hashable
    object should have a hash value that never changes during its lifetime, and it should be comparable to other
    objects. Immutable objects are hashable, because their hash value never changes.

    The `hash()` function returns the hash value of an object. The hash value is an integer that represents the object.
    """

    def is_hashable(obj):
        """Check if an object is hashable

        Args:
            `obj`: The object to check.

        Returns:
            `bool`: True if the object is hashable, False otherwise.
        """

        try:
            hash(obj)
        except TypeError:
            return False
        return True

    # Tuple with a list
    tp_1 = (1, 2, [3, 4])
    print(is_hashable(tp_1))  # False

    # Tuple with another tuple
    tp_2 = (1, 2, (3, 4))
    print(is_hashable(tp_2))  # True


if __name__ == "__main__":
    tuples_as_records_example()
    tuple_comparison_example()
    hashable_tuple_example()
