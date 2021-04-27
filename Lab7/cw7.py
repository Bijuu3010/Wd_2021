import numpy as np

macierz_1 = np.arange(0, 6).reshape(2, 3)
a = np.sin(macierz_1)

macierz_2 = np.arange(5, 11).reshape(2, 3)
b = np.cos(macierz_2)
print(a + b)