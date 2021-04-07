class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(f'rodzaj :{self.rodzaj}')
        print(f'dlugosc :{self.dlugosc}')
        print(f'szerokosc :{self.szerokosc}')

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    
    def wyswietl_dane(self):
        print(f'rozmiar :{self.rozmiar}')
        print(f'kolor :{self.kolor}')
        print(f'dla kogo :{self.dla_kogo}')

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
    
    def wyswietl_dane(self):
        print(f'rodzaj swetra :{self.rodzaj_swetra}')

welna = Material('welna', 72, 74)
ubranie = Ubrania('S', 'kremowy', 'dzieci')
sweter = Sweter('golf')
print(welna.wyswietl_nazwe())
print(ubranie.wyswietl_dane())
print(sweter.wyswietl_dane())

