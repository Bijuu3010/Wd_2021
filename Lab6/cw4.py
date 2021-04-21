import numpy as np

def zad_4(liczba, ilosc):
    return np.logspace(1, liczba, num=liczba, base=ilosc)

print(zad_4(2,4))