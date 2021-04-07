class Samogloski:
    
    def __init__(self, tekst):
        # isinstance sprawdza polimorficznie subklasy
        if isinstance(tekst, str):
            self.tekst = tekst
            self.index = 0
            self.baza = ['a',' ą', 'e', 'ę', 'i', 'o', 'u', 'y']
        else:
            raise TypeError("input must be a string")
         
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > len(self.tekst):
            raise StopIteration
        for index in range(len(self.tekst)):
            if self.tekst[self.index] in self.baza:
                retrun (self.tekst[self.index])

test = Samogloski('alą mę i yotu')
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
    

    
