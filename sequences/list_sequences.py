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


if __name__=='__main__':
    list_comprehension()
    cartesian_product_with_listcomp()
