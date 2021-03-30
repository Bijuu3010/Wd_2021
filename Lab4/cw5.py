class CiagArytmetyczny:
    an = {}
    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
    def pobierz_elementy(self, index, wartosc):
        self.an[index] = wartosc

    def wyswietl_dane(self):
        wynik = self.a1
        for i in range(1,self.n + 1):
            print(f'a({i}) = {wynik}')
            wynik += self.r
        
    def policz_elementy(self): 
        for i in range(1,self.n + 1):
            self.an[i] =  self.a1 + (i - 1) * self.r 
        return self.an

    def policz_sume(self):
        suma = 0
        # self.suma = ((self.a1 + self.an ) / 2) * self.n
        for i in self.an:
            suma += self.an[i]
        return f'wynik sumy {suma}'
    
# a1 = int(input("Podaj wartość a1 :"))
# r = int(input("Podaj różnicę r :"))
# n = int(input("Podaj n-ty element ciągu :"))

ciag = CiagArytmetyczny()

ciag.pobierz_elementy(1,1)
ciag.pobierz_elementy(3,3)
ciag.pobierz_elementy(2,2)
ciag.policz_sume()
print(ciag.policz_sume())

ciag.pobierz_parametry(1, 1, 10)
ciag.wyswietl_dane()
ciag.policz_elementy()
ciag.policz_sume()
print(ciag.policz_sume())
