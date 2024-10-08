"""Tuples vs Lists

This module demonstrates the differences between tuples and lists in Python.

Efficiency: 

Tuples are more efficient than lists because:
- The python compiler generates bytecode for a tuple in one operation, while for a list, the generated bytecode
  adds each element to the list one by one.
- For a tuple `t`, `tuple(t)` returns the reference same as of `t`. For a list `l`, `list(l)` makes a copy of the
  list and returns a new reference.
- Tuples have fixed length and so allocated the exact amount of memory required. Lists have variable length and
  so allocate extra memory to accommodate future growth.
- The references to each element in a tuple are stored in an array in the tuple struct. The list struct holds a 
  pointer to an array of references to the elements stored somewhere else in memory. This is called indirection,
  which is necessary because when a list grows, it may need extra space and in that case, the array of references
  may need to be reallocated. It makes CPU cache less effective.

Methods: 

[Chapter_02/07_comparing_list_and_tuple_methods.png]
"""

import sys
import timeit


def tuple_vs_list_generation_time():
    """Tuple vs List generation time

    This function demonstrates the time taken to generate a tuple and a list.
    """

    print("Tuple generation time:")
    print(timeit.timeit("(1, 2, 3, 4, 5,)", number=1000000))

    print("\nList generation time:")
    print(timeit.timeit("[1, 2, 3, 4, 5]", number=1000000))


def tuple_vs_list_copy():
    """Tuple vs List copy

    This function demonstrates the difference between copying a tuple and a list.
    """

    my_tuple = (1, 2, 3, 4, 5)
    my_list = [1, 2, 3, 4, 5]

    print("Tuple copy:")
    print(my_tuple is tuple(my_tuple))

    print("\nList copy:")
    print(my_list is list(my_list))


def tuple_vs_list_memory():
    """Tuple vs List memory

    This function demonstrates the memory usage of a tuple and a list.
    """

    my_tuple = (1, 2, 3, 4, 5)
    my_list = [1, 2, 3, 4, 5]

    print("Tuple memory:")
    print(sys.getsizeof(my_tuple))  # 80

    print("\nList memory:")
    print(sys.getsizeof(my_list))  # 104


if __name__ == "__main__":
    tuple_vs_list_generation_time()
    tuple_vs_list_copy()
    tuple_vs_list_memory()
