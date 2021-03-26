class CiagArytmetyczny:

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def wyswietl_dane(self):
        print(f'a1 = {self.a1}')
        print(f'r = {self.r}')
        print(f'n = {self.n}')
        print(f'an = {self.an}')
        print(f'suma = {self.suma}')   

    def policz_elementy(self):   
        self.an =  a1 + (n - 1) * r
        return self.an

    def policz_sume(self):
        self.suma = ((a1 + self.an ) / 2) * n
        return self.suma
    
    # def pobierz_elementy(self):   ####????
    
a1 = int(input("Podaj wartość a1 :"))
r = int(input("Podaj różnicę r :"))
n = int(input("Podaj n-ty element ciągu :"))

ciag = CiagArytmetyczny()

ciag.pobierz_parametry(a1,r,n)
ciag.policz_elementy()
ciag.policz_sume()
ciag.wyswietl_dane()
