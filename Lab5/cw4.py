class Point:
    counter = []

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def uptade(self, n):
        self.counter.append(n)

p1 = Point(0, 0)
p2 = Point(1, 1)
pusta = Point()
print(p1.counter)
p1.uptade('patryk')
print(p2.counter)
p1.uptade('pawel')
print(p1.counter)
p1.uptade('piotrek')
print(p2.counter)
pusta.counter.append('adam')
print(pusta.counter)
pusta.counter.append('Ania')
print(p2.counter)
