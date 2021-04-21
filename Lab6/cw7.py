import numpy as np

def zad_7(n):
    i = 1
    j = 2
    mat_diag = np.diag([2 for _ in range(n)])
    mat_diag_1 = [2 + 2 * i for _ in range(n - i)]
    mat_diag_2 = [2 + 2 * j for _ in range(n - j)]   
    print(mat_diag_1)

    mat_diag += np.diag(mat_diag_1, i)
    mat_diag += np.diag(mat_diag_2, j)
    mat_diag += np.diag(mat_diag_1, -i)
    mat_diag += np.diag(mat_diag_2, -j)

    return mat_diag

print(zad_7(3))
