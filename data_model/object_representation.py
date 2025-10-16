"""This program shows a basic usage of the __str__() and __repr__() methods. In general __str__() is intended
for users and __repr__() is intended for developers."""

from datetime import datetime

now = datetime.now()

print('__str__() representation of datetime.now(): ', now.__str__()) # This is showing the output in user friendly format
print('*'*40)
print('__repr__() representation of datetime.now(): ', now.__repr__()) # This includes more details which is more helpful for developers
print('*'*40)
print('just a regular print of datetime.now(): ', now) # This is just showing the same thing as the __str__() method; __str__() and __repr__() are usually not called directly
print('*'*80)
print('str(now): ', str(now))
print('repr(now): ', repr(now))


class Pet:
    '''An example using a new class: no special methods'''

    def __init__(self, pet_name, pet_age):
        self.name = pet_name
        self.age = pet_age

    
class EnhancedPed(Pet):
    '''An example using a new class with special methods'''

    def __init__(self, pet_name, pet_age):
        super().__init__(pet_name, pet_age)


    def __str__(self):
        return f"The name of my pet is {self.name} and it is {self.age} years old."


    def __repr__(self):
        return f"EnhancedPet('{self.name}', {self.age})"
    
    def talk(self):
        print('Bark bark...')



if __name__=='__main__':
    unfriendly_pet = Pet('Barky', 10)
    friendly_pet = EnhancedPed('Aira', 4)

    print('*'*40)
    print('str(unfriendly_pet): ', str(unfriendly_pet))
    print('repr(unfriendly_pet): ', repr(unfriendly_pet))
    print('*'*40)
    print('str(friendly_pet): ', str(friendly_pet))
    print('repr(friendly_pet): ', repr(friendly_pet))
    print('*'*40)
    print('friendly_pet.__dict__:', friendly_pet.__dict__)
    print('list(friendly_pet.__dict__.keys()):', list(friendly_pet.__dict__.keys()))
    print('dir(friendly_pet):', dir(friendly_pet))
    print('*'*40)
    for k, v in friendly_pet.__dict__.items():
        print(f'{k}: {v}')
