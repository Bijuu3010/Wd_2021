import numpy as np

def zad_5(wektor):
    return np.diag(range(wektor, 0, -1))

print(zad_5(3))
