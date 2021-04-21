import numpy as np

def Zad_3(n):
    a = np.arange(1, n * n + 1)
    b = a.reshape(n, n)
    return b

print(Zad_3(1))
print(Zad_3(2))
print(Zad_3(3))



