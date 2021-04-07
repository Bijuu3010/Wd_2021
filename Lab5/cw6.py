class Wspak:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

test = Wspak('Patryk')
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

test1 = Wspak([1, 9, 9, 2])
print(next(test1))
print(next(test1))
print(next(test1))
print(next(test1))