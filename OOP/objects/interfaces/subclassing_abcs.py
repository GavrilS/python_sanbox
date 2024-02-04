import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[positions] = value

    # Even if we don't need these methods for our class, MutableSequence demands we implement them for our class
    ## or there will be an error when we try to make an instance of it
    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)
    ##
