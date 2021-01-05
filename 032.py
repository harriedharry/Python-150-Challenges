import math

a = float(input("Radius of a cylinder: "))
c = float(input("Depth of the cylinder: "))
b = math.pi * (a ** 2) * c
print(round(b,3))
