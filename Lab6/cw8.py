import numpy as np

def zad_8(tablica, kierunek):

    if kierunek == 'pion':
        if tablica.shape[0] % 2 == 0:
            print('Nieparzysta liczba')
            

    # elif kierunek == 'poziom':
    #     if tablica.shape[1] % 2 == 0:
    #         print('Nieparzysta liczba')
            

zad_8(np.array([8]),'pion')
