lista = []
for i in range(1,50,1):
    if i % 4 == 0:
        lista += [i]
plik = open("zapis_cw1.py","w") 
plik.writelines(str(lista))       
plik.close()


