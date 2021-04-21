import numpy as np

def fibonacci(dlugosc):
    a = 0
    b = 1
    for _ in range(dlugosc):
        yield a
        b = a + b
        a = b - a
a = list(fibonacci(25))
print(np.array(a).reshape(5, 5))
