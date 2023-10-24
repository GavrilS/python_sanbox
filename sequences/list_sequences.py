"""
List comprehension is building up lists.
"""


def list_comprehension():
    symbols = '$c!@'
    # This is list comprehension
    codes = [ord(symbol) for symbol in symbols]
    print('codes: ', codes)


def cartesian_product_with_listcomp():
    """
    Cartesian product of T-shirts colors and sizes with list comprehension
    """
    colors = ['black', 'white']
    sizes = ['M', 'L', 'S']
    # Cartesian product arranging by color and than by size
    tshirts = [(color, size) for color in colors for size in sizes]
    print('tshirts by color/size: ', tshirts)

    # product arranged by size and than color
    tshirts2 = [(color, size) for size in sizes for color in colors]
    print('tshirts by size/color: ', tshirts2)


def in_place_operations_on_lists():
    l = [1, 2, 3]
    print('id(l): ', id(l))
    l *= 2
    print('l*=2 -> ', l)
    print('id(l): ', id(l))
    t = (1, 2, 3)
    print('id(t): ', id(t))
    t *= 2
    print('t *= 2 -> ', t)
    print('id(t): ', id(t))


def list_sorting():
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print('sorted: ', sorted(fruits))
    print('reverse: ', sorted(fruits, reverse=True))
    print('sorted by len: ', sorted(fruits, key=len))
    print('sorted by len in reverse: ', sorted(fruits, key=len, reverse=True))


if __name__=='__main__':
    list_comprehension()
    cartesian_product_with_listcomp()
    in_place_operations_on_lists()
    list_sorting()
