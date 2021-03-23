def ciag (a1, r, ile):
    an = a1 + (ile - 1) * r
    suma = ((a1 + an ) / 2) * ile
    return suma
print("Przykładowy ciag :", ciag(1,1,10))

a1 = int(input("Podaj a :"))
r = int(input("podaj r :"))
ile = int(input("podaj dlugosc ciagu :"))
print("Długość ciagu podana przez urzytkownika to :", ciag(a1,r,ile))