import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
  ranks = [i for i in range(2, 11)] + list('JQKA')
  suits = ['spades', 'diamonds', 'clubs', 'hearts']

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
    self._cards = [Card(rank, suit) 
                   for suit in self.suits 
                   for rank in self.ranks]
    
  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
  def filter_by_rank(self, rank):
    index = self.ranks.index(rank)
    return self._cards[index::4]
  
  def filter_by_suit(self, suit):
    index = self.suits.index(suit)
    return self._cards[index::13]
  
  def sort_key(self, card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = self.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
  
  def get_sorted(self):
    return sorted(self._cards, key=self.sort_key)
  