from director.bus import BusDirector
from director.walk import WalkDirector
from director.car import CarDirector

origin = 'Colonia Nápoles'
destiny = 'El Ángel de la Independencia'

WALK = WalkDirector.construct(origin, destiny)
CAR = CarDirector.construct(origin, destiny)
BUS = BusDirector.construct(origin, destiny)

print(WALK.construction())
print(CAR.construction())
print(BUS.construction())