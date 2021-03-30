class Robot:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def pokaz_gdzie_jestes(self):
        print(f'robot na pozycji ({self.x},{self.y})')
    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok
    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok
    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok
    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

robocik = Robot(0,0,1)
robocik.pokaz_gdzie_jestes()
robocik.idz_w_prawo(1)
robocik.idz_w_gore(1)
robocik.pokaz_gdzie_jestes()
robocik.idz_w_lewo(1)
robocik.idz_w_dol(1)
robocik.pokaz_gdzie_jestes()