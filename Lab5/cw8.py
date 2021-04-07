class Samogloski:
    
    def __init__(self, tekst):
        self.tekst = tekst
        self.index = 0
        self.baza = ['a', 'c']
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > len(self.tekst):
            raise StopIteration
        if self.baza:
            self.index += 1
        return self.tekst[self.index]

test = Samogloski('ala ma cota')
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
    
