class Ksztalty:

    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x
    
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, dodaj):
        suma = self.x + dodaj.x
        return suma


kw = Kwadrat(5)
kw1 = Kwadrat(6)
print(kw + kw1)