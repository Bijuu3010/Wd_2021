class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return f'Nazwa produktu: {self.nazwa_produktu} cena {self.cena_jed}zł/{self.jednostka_miary}'

    def ile_produktu(self):
        return f'Informacje o produkcie: {self.ilosc} {self.jednostka_miary}'

    def ile_kosztuje(self):
        cena = self.ilosc * self.cena_jed
        return f'Cena za kupiony produkt wynosi :{cena}'
        
koszyk = NaZakupy('Ziemiaki', 5, 'kg', 2)
print(koszyk.wyswietl_produkt())
print(koszyk.ile_produktu())
print(koszyk.ile_kosztuje())
