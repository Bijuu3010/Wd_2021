import numpy as np

macierz_1 = np.arange(0, 3)
macierz_1 *= 4

macierz_2 = np.arange(1, 4)
macierz_2 *= 5

print(macierz_1)
print(macierz_2)
print(macierz_1.dot(macierz_2))