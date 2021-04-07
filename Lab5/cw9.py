def parzyste(data):
    for i in range(len(data) - 1):
        i = i * 2
        yield data[i]

test = parzyste([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(next(test))
print(next(test))
print(next(test))
print(next(test))


