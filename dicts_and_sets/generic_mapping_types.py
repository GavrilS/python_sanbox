"""
collections.abs module -> provides the Mapping and MutableMapping ABCs to formalize the interface of dict and
similar types
"""
from collections import abc


def abc_mapping_test():
    """
    Using isinstance is better than checking if the var is of dict type, because then alternative mapping
    types can be used.
    """
    my_dict = {}
    print('isinstance(my_dict, abc.Mapping): ', isinstance(my_dict, abc.Mapping))


def declare_dict():
    a = dict(one=1, two=2)
    b = {'one': 1, 'two': 2}
    c = dict(zip(['one', 'two'], [1, 2]))
    d = dict([('two', 2), ('one', 1)])
    e = dict({'two': 2, 'one': 1})

    print('a==b==c==d==e: ', a==b==c==d==e)


def dict_comprehension_exmpl():
    dial_codes = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (81, 'Japan')
    ]

    country_code = {country: code for code, country in dial_codes}
    print('country_code: ', country_code)
    small_codes = {code: country for country, code in country_code.items() if code < 61}
    print('small_codes: ', small_codes)


if __name__=='__main__':
    abc_mapping_test()
    declare_dict()
    dict_comprehension_exmpl()
