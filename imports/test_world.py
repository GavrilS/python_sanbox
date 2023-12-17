import world

print('world: ', world)
print('world.africa: ', world.africa)
try:
    print('world.europe: ', world.europe)
except Exception as e:
    print('Exception trying to call world.europe: \n', e)

print('*'*40)

from world import europe

print('europe.greece: ', europe.greece)
try:
    print('europe.spain: ', europe.spain)
except Exception as e:
    print('Exception trying to call europe.spain: \n', e)

print('*'*40)

from world.europe import spain

print('spain: ', spain)

print('*'*40)

import world.africa.zimbabwe

print('world.africa.zimbabwe: ', world.africa.zimbabwe)
