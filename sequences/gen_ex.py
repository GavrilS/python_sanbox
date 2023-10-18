"""
List comprehension builds lists, but to fill out other sequence types gen. expr. are the way to go.
"""
import array


def initialize_tuple_with_genex():
    symbols = '$%#@!3weqw'
    tuple_from_genex = tuple(ord(symbol) for symbol in symbols)
    print('tuple_from_genex: ', tuple_from_genex)


def init_array_from_genex():
    symbols = '$%#@!3weqw'
    array_from_genex = array.array('I', (ord(symbol) for symbol in symbols))
    print('array_from_genex: ', array_from_genex)


def cartesian_product_from_genex():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print('tshirt: ', tshirt)


if __name__=='__main__':
    initialize_tuple_with_genex()
    init_array_from_genex()
    cartesian_product_from_genex()
