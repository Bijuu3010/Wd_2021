import numpy as np

macierz = np.arange(0, 12)
print(macierz)

macierz_1 = macierz.reshape(3, 4)
print(macierz_1.ravel())

macierz_2 = macierz.reshape(4, 3)
print(macierz_2.ravel())

macierz_3 = macierz.reshape(2, 6)
print(macierz_2.ravel())

# Są takie same