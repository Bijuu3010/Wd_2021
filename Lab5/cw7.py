class Parzyste:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 2
        return self.data[self.index]

test = Parzyste([0, 1, 2, 3, 4, 5, 6, 7 , 8])
print(next(test))
print(next(test))
print(next(test))
print(next(test))

