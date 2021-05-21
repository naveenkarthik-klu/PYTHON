
import math
pi = math.pi


def volume(r, h):
    return (1 / 3) * pi * r * r * h


def surfacearea(r, s):
    return pi * r * s + pi * r * r


radius = float(input("Enter radius of the cone: "))
height = float(input("Enter height of the cone: "))
slat_height = float(input("Enter slant height of the cone: "))
print("Volume Of Cone : ", volume(radius, height))
print("Surface Area Of Cone : ", surfacearea(radius, slat_height,))
