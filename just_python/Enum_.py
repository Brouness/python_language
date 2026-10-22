from enum import Enum

"""
Enums in Python are used to define a set of named constant values, They make code cleaner,
more readable and prevent using invalid values. Each member of an Enum has a name and a value.
also he can be used as an etarable object.
his type is enum so when you put car.SPRING == 1 its false not true even logicly it seems like
so you need to add str or other depends on your own target use
solution when you inherit use class name(str, Enum)
"""

class car(int, Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(type(car.SPRING))
if car.SPRING == 1:
    print("True")
for item in car:
    print(item.name)
for item in car:
    print(item.value)
print(item)
