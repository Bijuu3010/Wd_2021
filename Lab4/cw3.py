with open("zapis_cw3.py", "w") as plik:
    plik.write("Dodanie do pliku tekstu")
with open("zapis_cw3.py") as plik:
    open_txt = plik.read()
    print(open_txt)