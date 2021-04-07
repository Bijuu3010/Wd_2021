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

    def __ge__(self, other):
        if self.x >= other.x:
            return f'tak'
        else:
            return f'nie'
        
    def __gt__(self, other):
        if self.x > other.x:
            return f'tak'
        else:
            return f'nie'

    def __le__(self, other):
        if self.x <= other.x:
            return f'tak'
        else:
            return f'nie'

    def __lt__(self, other):
        if self.x < other.x:
            return f'tak'
        else:
            return f'nie'
        

kw = Kwadrat(5)
kw1 = Kwadrat(6)
print(kw + kw1)
print(f'{kw}')
print(f'{kw1}')
print('>=', kw >= kw1)
print('>', kw > kw1)
print('<=', kw <= kw1)
print('<', kw < kw1)