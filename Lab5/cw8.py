class Samogloski:
    
    def __init__(self, tekst):
        # isinstance sprawdza polimorficznie subklasy
        if isinstance(tekst, str):
            self.tekst = tekst
            self.index = 0
            self.baza = ['ą', 'c']
        else:
            raise TypeError("input must be a string")
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
    
