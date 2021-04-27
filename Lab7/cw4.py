import numpy as np

macierz_1 = np.arange(0, 3, dtype="int64")
print(macierz_1)

macierz_2 = np.arange(1.1, 1.6, 0.2, dtype="float")
print(macierz_2)

print(np.dot(macierz_1, macierz_2))