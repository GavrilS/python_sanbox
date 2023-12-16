"""A python program to showcase different uses of underscore(_)"""

""" 1. Use in interpreter:
# If can run the below in 'ipython' to verify the results
>>> 5 + 4
9
>>> _ # Stores the result of the above expression
9
>>> _ - 4
5
>>> new_var = _
>>> new_var
5
"""


def ignore_values(values):
    a, _, b = values
    print(a, b)


def use_in_looping():
    print('for _ in range(5):')
    for _ in range(5):
        print(_)

    print('*'*40)
    languages = ['Java', 'Python', 'JavaScript', 'C#']
    print('for _ in languages:')
    for _ in languages:
        print(_)

    print('*'*40)
    _ = 5
    print('while _ < 10:')
    while _ < 10:
        print(_, end=' ')
        _ += 1
    print()


def separate_number_digits():
    mill = 1_000_000
    binary = 0b_0010
    octa = 0o_64
    hexa = 0x_23_ab

    print('Numbers separated by underscore(_):')
    print('mill: ', mill)
    print('binary: ', binary)
    print('octa: ', octa)
    print('hexa: ', hexa)
    

def naming():
    '''Underscore(_) can be used to name variables: 
        _variable, 
        variable_, 
        __variable, 
        __variable__
    '''
    pass


if __name__=='__main__':
    print('ignore_values((1,2,3)):')
    ignore_values((1,2,3))
    print('*'*80)
    use_in_looping()
    print('*'*80)
    separate_number_digits()
