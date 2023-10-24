"""
Tuples are immutable lists, but they can be used for much more than just that:
- records - holds the data for one field and the position of the item gives it meaning
- namedtuples - each field in the tuple has a name, in essence it mirrors a class with fields -> example
is the Deck named tuple...
"""
from collections import namedtuple


def tuples_as_records():
    # Latitude and longitude...
    coordinates = (33.345, -118.408)

    # related pieces of information
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

    traveler_ids = [('USA', '3119855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)



def tuple_unpacking():
    a,b = 3, 4
    print(f'a, b: {a}, {b}')

    a,b = b,a
    print(f'a,b: {a},{b}')

    a,b,*rest = range(5)
    print(f'a,b,*rest: {a},{b},{rest}')

    a,b,*rest = range(3)
    print(f'a,b,*rest: {a},{b},{rest}')

    a,b,*rest = range(2)
    print(f'a,b,*rest: {a},{b},{rest}')

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))



def namedtuple_ex():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print('tokyo: ', tokyo)
    print(f'tokyo.population: {tokyo.population}')
    print(f'tokyo[1]: {tokyo[1]}\n')

    # namedtuple attributes
    print(f'City._fields: {City._fields}\n')
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.000, 77.2000))
    delhi = City._make(delhi_data)
    print('delhi._asDict: ', delhi._asdict())
    for key, value in delhi._asdict().items():
        print(key + ':', value)


def slices_ex():
    l = list(range(10))
    print('l: ', l)
    l[2:5] = [20, 30]
    print('l[2:5] = [20, 30] -> ', l)
    del l[5:7]
    print('del l[5:7] -> ', l)
    l[3::2] = [11, 12]
    print('l[3::2] -> ', l)
    try:
        l[2:5] = 100
    except Exception as e:
        print('l[2:5] = 100 -> ', str(e))

    l[2:5] = [100]
    print('l[2:5] = [100] -> ', l) 




if __name__=='__main__':
    tuples_as_records()
    tuple_unpacking()
    namedtuple_ex()
    slices_ex()
