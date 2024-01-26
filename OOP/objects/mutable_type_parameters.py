"""
It is not a good idea to use mutable types as function defaults.
"""

class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Busses haunted by ghost passengers example
bus1 = HauntedBus(['A', 'B'])
print('bus1.passengers: ', bus1.passengers)
bus1.pick('D')
bus1.drop('A')
print('bus1.pick("D")')
print('bus1.drop("A")')
print('bus1.passengers: ', bus1.passengers)
bus2 = HauntedBus()
bus2.pick('C')
print('bus2.passengers: ', bus2.passengers)
bus3 = HauntedBus()
print('bus3.passengers: ', bus3.passengers)
bus3.pick('D')
print('bus2.passengers: ', bus2.passengers)
print('bus3.passengers: ', bus3.passengers)
print('bus2.passengers in bus3.passengers: ', bus2.passengers in bus3.passengers)
print('bus1.passengers: ', bus1.passengers)
