def sorting_with_strings():
    """String sorting

    Strings are sorted lexicographically by default. This means that the Unicode code points
    of the characters are compared. This is why uppercase letters come before lowercase
    letters in the sorted output.
    """
    fruits = ["banana", "Apple", "mango", "kiwi", "orange", "grape"]
    print("Before sorting:")
    print("fruits:", fruits)

    # The sorted() function returns a new list and doesn't modify the original list.
    print("Sorted fruits:", sorted(fruits))
    print("After sorting:")
    print("fruits:", fruits)

    print("\nSorting with a custom key:")
    print("Sorted fruits (case-insensitive):", sorted(fruits, key=str.casefold))
    print("Sorted fruits (based on length):", sorted(fruits, key=len, reverse=True))


def sorting_with_dicts():
    posts = [
        {"title": "Post 1", "views": 10, "ratings": [5, 4.4, 3.9, 4.1, 4.7]},
        {"title": "Post 2", "views": 15, "ratings": [4.9, 4.2, 4.8, 4.5, 4.6]},
        {"title": "Post 3", "views": 25, "ratings": [4.1, 4.2, 4.3, 4.4, 4.5]},
        {"title": "Post 4", "views": 20, "ratings": [4.6, 4.7, 4.8, 4.9, 5.0]},
    ]
    # sorted(posts)
    # This will raise a TypeError because the Timsort doesn't support dicts.

    # Sort by views
    views_key = lambda post: post["views"]
    print("Sorted by views:")
    print(sorted(posts, key=views_key, reverse=True))

    # Sort by average rating
    rating_key = lambda post: (
        sum(post["ratings"]) / len(post["ratings"]) if post["ratings"] else 0
    )
    print("\nSorted by average rating:")
    print(sorted(posts, key=rating_key, reverse=True))


if __name__ == "__main__":
    # sorting_with_strings()
    sorting_with_dicts()
