"""Concatenating and repeating iterables using + and * operators"""


def simple_examples():
    l1 = ["oranges", "mangoes", "apples"]
    l2 = ["carrots", "potatoes", "onions"]
    print("l1:", l1)
    print("l2:", l2)

    # When + is used to concatenate two iterables, both the operands
    # must be of the same type. It doesn't change the original iterables,
    # but creates a new iterable of the same type.
    l3 = l1 + l2
    print("\nAfter concatenating l1 and l2:")
    print("l3:", l3)

    # When * is used to repeat an iterable, one of the operands must be an
    # integer and the other must be an iterable. It doesn't change the original
    # iterable, but creates a new iterable of the same type.
    l4 = l1 * 3
    print("\nAfter repeating l1 thrice:")
    print("l4:", l4)

    # Using * to repeat a string or any other immutable sequence is a common
    # idiom in Python. But using it for mutable sequences like lists can lead
    # to unexpected results. For example, if you use * to repeat a list of lists,
    # you'll end up with a list of references to the same list. So, changing one
    # element will change all the elements, which we don't want.
    l5 = [[0] * 2] * 3  # This will create a list of 3 references to the same [0, 0]
    print("\nAfter repeating [0, 0] thrice using *:")
    print("l5:", l5)
    l5[0][0] = 1
    print("l5 after changing l5[0][0] to 1:")
    print("l5:", l5)

    # To avoid this, you can use a list comprehension to create a list of distinct
    # lists. This way, changing one element won't affect the others.
    l6 = [[0] * 2 for _ in range(3)]
    print("\nAfter repeating [0, 0] thrice using LC:")
    print("l6:", l6)
    l6[0][0] = 1
    print("l6 after changing l6[0][0] to 1:")
    print("l6:", l6)

    # To add more elements to an iterable using concatenation or repetition, we can use the
    # += and *= operators respectively.
    # If the iterable is mutable, and implements the __iadd__ and __imul__ methods, the
    # elements will be added in-place.
    print("\nBefore adding more elements to l1:")
    print("id(l1):", id(l1))
    l1 += ["bananas", "grapes"]
    print("After adding more elements to l1:")
    print("l1:", l1)
    print("id(l1):", id(l1))

    # Otherwise, __add__ and __mul__ will be called, and a new iterable will be created
    # and assigned to the variable. This makes the += and *= operators less efficient for
    # immutable sequences. However, str is an exception to this rule, because it's optimized
    # by CPython for its common use cases.
    # Trying the same with a string and a tuple (both immutable sequences).
    s1 = "hello"
    print("\ns1:", s1)
    print("id(s1):", id(s1))
    s1 += " world"
    print("After adding more elements to s1:")
    print("s1:", s1)
    print("id(s1):", id(s1))

    t1 = (10, 20, 30)
    print("\nt1:", t1)
    print("id(t1):", id(t1))
    t1 *= 3
    print("After repeating t1 thrice:")
    print("t1:", t1)
    print("id(t1):", id(t1))


def assignment_puzzler():

    # t being a tuple is immutable, but the list inside it is mutable at index 2.
    t = (1, 2, [30, 40])

    # This will raise TypeError because tuple assignment is not supported.
    # t[2] += [50, 60]

    # Let's see what happens when we try to do catch the exception.
    try:
        t[2] += [50, 60]
    except TypeError:
        print("Caught TypeError")

    print(t)  # Output: (1, 2, [30, 40, 50, 60])
    # This is strange because the exception is caught, but the list is still modified.
    # The bytecode for the expression `t[2] += [50, 60]` first fetches the list at index 2
    # and then applies += to it. Being mutable, the list is modified in-place. But when the
    # the new list is assigned back to the tuple, it raises a TypeError because tuple assignment
    # is not supported.
    import dis

    print("\nBytecode for `t[2] += [50, 60]`:")
    dis.dis("t[2] += [50, 60]")

    # It means that augmented assignment operators like +=, -=, *=, etc., are not atomic. We
    # shouldn't use mutable items in tuples.

    # Even if we want to, then we should do item assignment, instead we can use methods like
    # list.extend() or list.append() to modify the list in-place. By looking at the bytecode
    # for the expression `t[2].extend([50, 60])`, we can see that it doesn't involve tuple
    # assignment, and the list is modified in-place.
    print("\nBytecode for `t[2].extend([50, 60])`:")
    dis.dis("t[2].extend([50, 60])")


if __name__ == "__main__":
    # simple_examples()
    assignment_puzzler()
