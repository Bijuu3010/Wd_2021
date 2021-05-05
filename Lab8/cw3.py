import pandas as pd
import numpy as np
from datetime import date

df = pd.read_csv('zamowienia.csv', header=0, sep=";")

#A
nazwiska = df["Sprzedawca"]
print(nazwiska.unique())

#B
zamowienie = df.sort_values(by=["Utarg"], ascending=False).head(5)
print(zamowienie)

#C
ilosc = df.groupby("Sprzedawca")["Utarg"].count().reset_index(name="Ilosc")
print(ilosc)

#D
suma_zamowienia = df.groupby("Kraj")["Utarg"].sum().reset_index(name="Suma zamowienia")
print(suma_zamowienia)

#E
zamowienia_2005 = df.copy()
zamowienia_2005['year'] = pd.DatetimeIndex(zamowienia_2005['Data zamowienia']).year
zamowienia_2005 = zamowienia_2005.groupby(["year",'Kraj']).agg({"idZamowienia":['count']})
print(zamowienia_2005.index.values[5],zamowienia_2005.values[5])

#F
zamowienia_2004 = df.copy()
zamowienia_2004['year'] = pd.DatetimeIndex(zamowienia_2004['Data zamowienia']).year
zamowienia_2004 = zamowienia_2004.groupby(["year"]).agg({"Utarg":['mean']})
print(zamowienia_2004.index.values[1],zamowienia_2004.values[1][0])

#G
zamowienia_2004.to_csv('zamowienia_2004.csv', index=False)
zamowienia_2005.to_csv('zamowienia_2005.csv', index=False)
