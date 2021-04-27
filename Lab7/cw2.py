import numpy as np

macierz_a= np.arange(0, 9).reshape(3,3)
print("3x3")
print(macierz_a)
print('kolumny', macierz_a.min(axis=0))
print('rzędy', macierz_a.min(axis=1))

macierz_b= np.arange(0, 16).reshape(4,4)
print("4x4")
print(macierz_b)
print('kolumny', macierz_b.min(axis=0))
print('rzędy', macierz_b.min(axis=1))