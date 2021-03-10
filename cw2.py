#zadanie 1

#text = input("Podaj imie \n")
#space = f"Ilosc spacji w tekscie wynosi {text.count(' ')} razy"
#print(space)

#zadanie 2

import sys

# print("Podaj a")
# a = sys.stdin.readline()
# print("Podak b")
# b = sys.stdin.readline()
# c = int(a) * int(b)
# sys.stdout.write(str(c))

#zadanie 4

import math 

#x = int(input("Podaj liczbe \n"))

#if x < 0:
#    x = math.fabs(x)
#    print(f"Wartość bezwgledna z liczby x wynosi {x}")
#else:
#    print(f"Wartość bezwgledna z liczby x wynosi {x}")

#zadanie 5

a = int(input("Podaj liczbe \n"))
b = int(input("Podaj liczbe \n"))
c = int(input("Podaj liczbe \n"))

if 0 <= a and a <= 10:
    print("miesci sie w przedziale")
    
    if a > b or b > c:
        print(" warunek a>b b>c spełniony 5")
    
    else:
        print("warunek a>b b>c nie spełniony ")

else:
    print("nie miesci sie w przediale")

     





