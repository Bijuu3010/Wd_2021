def proste (a1, a2):

    if a1 == a2:
        print("rownolegle")
        return (a1, a2)
    elif (a1 * a2) == -1:
        print("prostopadle")
        return (a1 * a2)
    else:
        return "nie jest rownolegly ani prostopadly"

a = int(input("podaj a1 :"))
b = int(input("podaj a2 :"))
print(proste(a,b)