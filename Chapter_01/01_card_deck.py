"""Card Deck

This module contains the implementation of a French Deck of cards.
"""

import collections

# Named tuple to represent a card
# If we create a simple tuple, we wouldn't be able to set the values
# by field names, and making use of indices for that purpose would be
# confusing. This problem is solved by `namedtuple`. Commonly used in
# records from database.
# Here, `rank` is the value of the card and `suit` is the category of
# the card.
# Example: `card = Card(rank="2", suit="hearts")`
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """A collection of 52 playing cards"""

    ranks = [i for i in range(2, 11)] + list("JQKA")
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        """
        Initialize the deck of cards

        Order example --
        2 of spades, 2 of diamonds, 2 of clubs, 2 of hearts,
        3 of spades, 3 of diamonds, 3 of clubs, 3 of hearts,
        ...

        General Formula --
        `Card(rank, suit) = index(rank) * len(suits) + index(suit`)
        """
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def filter_by_rank(self, rank):
        """Filter the cards by rank

        Args:
            rank (`str`): The rank of the cards to be filtered.

        Returns:
            `list`: The list of cards with the specified rank.
        """
        index = self.ranks.index(rank)
        return self._cards[index::4]

    def filter_by_suit(self, suit):
        """Filter the cards by suit

        Args:
            suit (`str`): The suit of the cards to be filtered.

        Returns:
            `list`: The list of cards with the specified suit.
        """
        index = self.suits.index(suit)
        return self._cards[index::13]

    def sort_key(self, card):
        """Sort key for the cards

        The cards are sorted by suit and then by rank.

        Args:
            card (`Card`): The card to be sorted.

        Returns:
            `int`: The sort key for the card.
        """

        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    def get_sorted(self):
        """Get the sorted list of cards

        Returns:
            `list`: The sorted list of cards.
        """

        return sorted(self._cards, key=self.sort_key)
