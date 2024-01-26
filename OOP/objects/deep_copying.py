import copy

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Example starts here
bus1 = Bus(['A', 'B', 'C'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(f"id(bus1) - {id(bus1)};\nid(bus2) - {id(bus2)};\nid(bus3) - {id(bus3)}")
print('bus1.drop("B")')
bus1.drop('B')
print('bus1.passengers: ', bus1.passengers)
print('bus2.passengers: ', bus2.passengers)
print('bus3.passengers: ', bus3.passengers)
print(f"id(bus1) - {id(bus1)};\nid(bus2) - {id(bus2)};\nid(bus3) - {id(bus3)}")
