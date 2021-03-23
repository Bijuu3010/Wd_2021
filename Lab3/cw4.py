def monotonicznosc (a, b):
    if a > 0:
        print("rosnący")
        return a
    elif a < 0:
        print("malejący")
        return a
    else:
        print("stały")
        return a

a = int(input("podaj a :"))
b = int(input("podaj b :"))
print(monotonicznosc(a,b))