import math 

def kolo (a, b, x, y):

    r = ((x - a) ** 2 + (y - b)  ** 2)
    promien = math.sqrt(r)
    return promien

print(kolo(-1, -6, -5, -3))