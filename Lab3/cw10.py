# zadanie 10

# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print(f'Lubię {cos}', end='')
#         if len(rzeczy[cos]) > 0:
#             print(f', takie jak {rzeczy[cos]}.')

# to_lubie(slodycze="czekolada", rozrywka=["disco-polo", "moda na sukces"])  

def produkty(** zakupy):
   
    for ile in zakupy:
        print(f'{zakupy}')
        suma = 0.0
        for i in zakupy:
            suma += float(zakupy[i])
        return suma
        
print('lista wszystkich zakupów',produkty(banan = 6, mleko = 5, woda = 2, chleb = 1))