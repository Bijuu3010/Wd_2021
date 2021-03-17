#zadanie 1

#text = input("Podaj imie \n")
#space = f"Ilosc spacji w tekscie wynosi {text.count(' ')} razy"
#print(space)

#zadanie 2

# import sys

# print("Podaj a")
# a = sys.stdin.readline()
# print("Podak b")
# b = sys.stdin.readline()
# c = int(a) * int(b)
# sys.stdout.write(str(c))

#zadanie 4

# import math 

#x = int(input("Podaj liczbe \n"))

#if x < 0:
#    x = math.fabs(x)
#    print(f"Wartość bezwgledna z liczby x wynosi {x}")
#else:
#    print(f"Wartość bezwgledna z liczby x wynosi {x}")

#zadanie 5

# a = int(input("Podaj liczbe \n"))
# b = int(input("Podaj liczbe \n"))
# c = int(input("Podaj liczbe \n"))

# if 0 <= a and a <= 10:
#     print("miesci sie w przedziale")
    
#     if a > b or b > c:
#         print(" warunek a>b b>c spełniony 5")
    
#     else:
#         print("warunek a>b b>c nie spełniony ")

# else:
#     print("nie miesci sie w przediale")

#zadanie6

# a = int(input("Liczba podzielna przez \n"))
# b = int(input("Z jakiego zakresu liczb \n"))

# for i in range(b+1):
#     if i % a == 0:
#         print(i)

#zadanie 7

# a = int(input("Ile razy ma pobrac liczbe \n"))

# for i in range(a+1):
#     b = int(input("Podaj liczbe"))
#     print(b*b)

#zadaie 8

# lista = []

# liczba = int(input("Ile liczb dodac do listy"))
# licznik = 0
# while (licznik != liczba):
#     a = int(input("podaj liczbe \n "))
#     lista.append(a)
#     licznik += 1
# print(lista)

#zadanie 9

# liczba = str(input("podaj ciag liczb \n"))
# licznik = 0
# suma = 0
# index = 0
# while licznik != len(liczba):
#     cyfra = int(liczba[index])
#     index += 1
#     licznik += 1
#     suma = suma + cyfra
# print(suma)

#zadania 10

# a = int(input("podaj wysokos wieży: "))
# znak = 'A' 
# if a >=0 and a <= 10:
#     for i in range(a+1):
#         znak = 'A' * i
#         print(znak)
# else:
#     print("nie miesci sie w przedzialle 0-10")

#zadanie 11




#zadanie 12

# i = 1
# j = 1
# while i < 11:
#     j = 1
#     while j < 11:
#         print(i, '*', j, '=', i * j)
#         j += 1
#     i += 1
# for i in range (1, 11):
#     for j in range(1, 11):
#         print(i, '*', j, '=', i * j)
