""" 
There are a number of ways to deal with the need for constants e.g. pi
The most reliable way to ensure a constant value is used is to import it from:
    - an external package e.g. math (for well known constants like pi)
    - a user-defined library for program-specific constants
"""

import spheres.sphere as sphere
from spheres.dimensions.dimensions import *
import sys

# 3.2
A = sphere.area(5)
print(f'The surface area is {A} m2')

# 3.5
A = sphere.area(radius)
V = sphere.volume(radius)

print(f'The area is {A} and the volume is {V}')


# 4.2
sys.path.append('../')
import cube

P = cube.perimeter(radius)
print(f'The perimeter of the cube is {P}')

