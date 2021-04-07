import itertools as it
# combinations('ABCD', 2)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
wynik = list(it.combinations(lista, 3))
print(wynik)