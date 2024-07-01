# The Python Data Model

## Overview
- It's intriguing that we use `len(collection)` instead of `collection.len()` in Python.
- Some things are just Pythonic. We need to understand the Python data model, which includes the common APIs to make use of idiomatic features.
- We can think of Python as a framework including sequences, functions, iterators, coroutines, classes, context managers, and so on.
- Python also has special methods, whose names are formatted with leading and trailing double underscores.

## Key Points
- `collections.namedtuple` is used to create tuples with each position named to a particular field.
- `sorted(iterable, key, reverse)`, where `key` is a function that takes an `item` as an argument and returns a value used for sorting order, and `reverse` is a `bool` value defaulting to `False`, used to specify whether the order should be ascending or descending.

## Special Methods
- `__len__()` for determining length.
- `__getitem__()` for item access using `obj[index]` syntax. Also supports slicing, iteration, inclusion, reversing, sorting, etc.
- We shouldn't call the special methods explicitly; let Python do it itself. Neither should we define any custom method using the `__*__()` format, as it might clash with any of the existing special methods.
- The string representation of an object is defined in `__repr__()` and it has a default implementation. It should be in such a way that the representation can be used to reconstruct the same object. `__str__()`, however, is used by `print()`, and if not implemented, uses `__repr__()` as a fallback.
- `__bool__()` is called when we use `bool(obj)`, and it determines the truth value of an object. Instances of all user-defined classes are truthy unless `__bool__()` or `__len__()` are explicitly defined.
- For built-in types like `str`, `list`, `bytearray`, `np.ndarray`, etc., variable-sized collections written in C are used, which include a `struct PyVarObject`, having an `ob_size` field. So for these objects, `__len__()` uses the `ob_size` value for length, and hence turns out to be even faster.
- When we loop through an iterable, e.g., `for i in x`, Python creates an iterator using, say `it = iter(x)` and keeps on calling `i = next(it)` until a `StopIteration` exception is raised. These are handled using the special methods `__iter__()` and `__next__()` respectively.
- `__add__(self, other)` and `__mul__(self, other)` are used for overloading the `+` and `*` operators. They return the same type as `self` and do not modify `self`.
- `__abs__()` is called when we use `abs(obj)`.
- In `__repr__()` we should use `!r` in `f-strings` as a good practice to show values in standard representations.

## Collection API
- ABCs stand for "Abstract Base Classes" - must be implemented in a concrete subclass. The same goes for abstract methods.
- These ABCs are defined in the `collections.abc` library. Some of them are:
  - `Iterable` for unpacking and iteration.
  - `Sized` to be utilized in the `len` function.
  - `Container` for inclusion checks - `in` operator.
  - `Reversible` to be utilized in `reversed`.
  - `Sequence` for ordered collections, such as `str`, `list`, `tuple`.
  - `Mapping` for key-value collections, such as `dict`, `collections.defaultdict`.
  - `Set` for unordered collections, such as `set`, `frozenset`.
