class Slowa:

    def sprawdz_czy_palindrom(self):
        #1 przykład

        j = 0
        licznik = 0
        for i in range(len(txt)-1, -1, -1):
            if txt[j] == txt[i]:
                licznik += 1
            j  += 1
        if len(txt) == licznik:
            print('palindrom')
        else:
            print('nie jest palindorm')

        #2 przykład
        
        # txt_p = txt[::-1]
        # if txt == txt_p:
        #     return 'Jest to palindrorm'
        # else:
        #     return 'Nie jest to palindrom'

        #3 przyklad

        # txt_1 = txt
        # txt_1 = txt.casefold()
        # rev_txt = reversed(txt)
        # if list(txt_1) == list(rev_txt):
        #     return 'Jest to palindrom'
        # else:
        #     return 'Nie jest to palindrom'
    def sprawdz_czy_metagrama(self):

        licznik = 0
        index = 0
        wynik_napis_true = 0
        if len(txt1) != len(txt2):
            return 'dlugosc tekstow sie nie zgadza'
        else:
            while licznik != len(txt1):
                licznik +=1
                if txt1[index] != txt2[index]:
                    wynik_napis_true += 1
                index +=1
            if wynik_napis_true == 1:
                return 'jest metagramem'
            else:
                return 'nie jest metagaramem'

    def sprawdz_czy_anagrama(self):

        if sorted(txt1) == sorted(txt2):
            return 'jest to anagram'
        else:
            return 'nie jest to anagram'
    def wyswietl_wyrazy(self):
        print(f'Pierwszy wyraz "{txt1}" Drugi wyraz "{txt2}"')
        print(f'wyraz "{txt}" ktory jest sprawdzany czy jest to palindrom')

napis = Slowa()
txt = 'kajak'
txt1='kra'
txt2='rak'
# txt1 = str(input('Podaj pierwsze słowo :'))
# txt2 = str(input('Podaj drugie słowo :'))
napis.wyswietl_wyrazy()
print(napis.sprawdz_czy_metagrama())
print(napis.sprawdz_czy_anagrama())
napis.sprawdz_czy_palindrom()



