import numpy as np

txt1 = 'patryk'
txt2 = 'robert'
j = 0
mat_diag = np.diag([txt1[i] for i in range(6)])
mat_diag_1 = [txt2[j] for j in range(6 - j)]
# mat_diag += np.diag(mat_diag_1, j)
print(mat_diag)