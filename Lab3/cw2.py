import random as rand

matrix = [[rand.randint(0,9) for i in range(4)] for j in range(4)]
przekatna = [matrix[i][j] for i in range(4) for j in range(4) if i == j]
for x in range(4):
    index = x
    print(matrix[index])
print(przekatna)