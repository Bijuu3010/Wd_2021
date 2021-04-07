
def fibonacci(dlugosc):
    a = 0
    b = 1
    for _ in range(dlugosc):
        yield a
        b = a + b
        a = b - a

print(list(fibonacci(20)))