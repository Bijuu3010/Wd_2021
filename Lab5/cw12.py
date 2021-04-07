def miesiace(dlugosc):
    kal = ['styczen', 'luty', 'marzec',
                'kwiecien', 'maj', 'czerwiec',
                'lipiec', 'sierpien', 'wrzesien',
                'pazdziernik', 'listopad', 'grudzien']
    for i in range(dlugosc):
        yield kal[i]

print(list(miesiace(3)))
print(list(miesiace(6)))
print(list(miesiace(9)))
print(list(miesiace(12)))
# print(next(miesiac))
# print(next(miesiac))
# print(next(miesiac))