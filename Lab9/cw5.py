import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("zamowienia.csv", header=0, sep=";")

liczba = df.groupby("Sprzedawca")["Utarg"].count()
wykres = liczba.plot.bar()
wykres.set_ylabel("Ilość zamówień")
wykres.set_xlabel("Sprzedawca")
plt.title("Ilość złożonych zamówień przez sprzedawców")
plt.show()