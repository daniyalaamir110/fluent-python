from collections import namedtuple
from pprint import pprint


def tshirt_example():
    """T-Shirt Example

    Create a list of T-Shirts with different colors and sizes.
    Using multiple for loops in a list comprehension will create
    a cartesian product.
    """

    colors = ["red", "green", "blue"]
    sizes = ["S", "M", "L"]

    TShirt = namedtuple("TShirt", ["color", "size"])

    # Cartesian product: sizes x colors
    tshirts = [TShirt(color=color, size=size) for color in colors for size in sizes]

    pprint(tshirts)


if __name__ == "__main__":
    tshirt_example()
