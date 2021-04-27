import numpy as np

macierz = np.arange(0, 81).reshape(9, 9)
print(macierz)

# macierz_1 = np.arange(0, 81).reshape(1, 81)
# print(macierz_1)

# macierz_2 = np.arange(0, 81).reshape(3, 27)
# print(macierz_2)

macierz_3 = np.arange(0, 81).reshape(27, 3)
print(macierz_3)

# macierz_4 = np.arange(0, 81).reshape(81, 1)
# print(macierz_4)

# Możliwości 1x81, 3x27, 9x9, 27x3, 81x1, podzielne przez 81