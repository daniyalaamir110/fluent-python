"""Slicing

Slicing is a powerful feature of Python that allows you to extract a subset of a 
list, tuple, or string. The syntax for slicing is `somelist[start:stop:step]`.
"""


def slicing_example():
    l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print(l[2:5])
    print(l[2:])
    print(l[:5])
    print(l[1::2])
    print(l[::-1])

    l[2:5] = [300, 400]
    print(l)


def slice_object_example():
    """Slice object example

    The slice object allows you to define a slice once and use it multiple times.
    This example demonstrates how to use a slice object to extract information from
    a fixed-width record string.
    """

    invoice = (
        "0.....6.................................40........50...55........\n"
        "1909  Pimoroni PiBrella                 $17.50    3    $52.50\n"
        "1489  6mm Tactile Switch x20            $4.95     2    $9.90\n"
        "1510  Panavise Jr. - PV-201             $28.00    1    $28.00\n"
        "1601  PiTFT Mini Kit 320x240            $34.95    1    $34.95\n"
    )

    # Split the invoice into line_items
    line_items = tuple(map(str.strip, invoice.split("\n")))[2:-1]

    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 50)
    QUANTITY = slice(50, 55)
    ITEM_TOTAL = slice(55, None)

    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])


if __name__ == "__main__":
    slicing_example()
    # slice_object_example()
