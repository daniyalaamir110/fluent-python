def metro_areas_table_example():
    """Metro Areas Table Example

    This function demonstrates the use of format specifications to create a table of metro areas.
    """

    metro_areas = (
        ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
        ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
        ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
        ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
        ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
    )

    print(f"{'Area':15} | {'Latitude':>9} | {'Longitude':>9}")
    print(f"{'-'*16}+{'-'*11}+{'-'*10}")

    for name, _, _, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(f"{f'{name}':15} | {latitude:9.4f} | {longitude:9.4f}")


if __name__ == "__main__":
    metro_areas_table_example()
