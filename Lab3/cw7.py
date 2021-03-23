import math as m

def pitagors (a, b):

    c = m.sqrt(a ** 2 + b ** 2)
    return c 

a = float(input("Podaj a :"))
b = float(input("podaj b :"))

print("Wynik dlugośći przeciwprostokątnej to :", pitagors(a, b))