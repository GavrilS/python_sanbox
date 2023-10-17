"""
Card deck implemented with the help of special methods to make it behave in a more pythonic way.
Special methods implemented in the class:
__init__; __len__; __getitem__
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class BasicDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


    def __len__(self):
        return len(self._cards)

    
    def __getitem__(self, position):
        return self._cards[position]



if __name__=='__main__':
    deck = BasicDeck()
    print('len(deck): ', len(deck))
    print('deck[0]: ', deck[0])
    print('deck[-1]: ', deck[-1])

    from random import choice
    for i in range(5):
        print(choice(deck))

    # supports slicing
    print('deck[:3]: ', deck[:3])

    # is iterable
    print('is iterable***')
    counter = 0
    for card in deck:
        counter += 1
        print(card)
        if counter > 10:
            break
    print('in reverse with __reversed__ special method implementation***')
    for card in reversed(deck):
        counter += 1
        print(card)
        if counter > 20:
            break
    # works with the in operator
    print('Card("A", "spades") in deck', Card("A", "spades") in deck)
