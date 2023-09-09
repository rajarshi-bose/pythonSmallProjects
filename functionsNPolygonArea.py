from math import *
side = float(input("Please enter the side length: "))

def area_polygon(side,number):
    circumradius = side/(2 * tan(pi/number))
    area = (side * number * circumradius)/2
    return area


a_triangle = area_polygon(side,3)
a_square = area_polygon(side,4)
a_pentagon = area_polygon(side,5)
a_dodecagon = area_polygon(side,12)
print(f'A triangle with side {side:.2f} has area {a_triangle:.3f}')
print(f'A square with side {side:.2f} has area {a_square:.3f}')
print(f'A pentagon with side {side:.2f} has area {a_pentagon:.3f}')
print(f'A dodecagon with side {side:.2f} has area {a_dodecagon:.3f}')
