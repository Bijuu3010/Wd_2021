class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return f'{self.imie}, {self.nazwisko}'

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja
    
    def przedstaw_sie(self):
        return f'{self.imie} {self.nazwisko}, i zarabiam {self.pensja}'

class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return f'{self.imie} {self.nazwisko}, jestem menadzerem i zarabiam {self.pensja}'


patryk = Pracownik("Patryk", "Kowalski", 2000)
pawel = Menadzer("Pawel", "Nowak", 5000)

print(patryk.przedstaw_sie())
print(pawel.przedstaw_sie())
print('######Isinstance')
print(isinstance(patryk, Osoba))
print(isinstance(patryk, Pracownik))
print(isinstance(patryk, Menadzer))
print(isinstance(pawel, Osoba))
print(isinstance(pawel, Pracownik))
print(isinstance(pawel, Menadzer))
print('######Issubclass')
print(issubclass(Pracownik, Osoba))
print(issubclass(Pracownik, Pracownik))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Menadzer, Menadzer))


