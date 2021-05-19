import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

wszystkie_lata = df.groupby(["Rok", "Plec"])["Liczba"].sum().reset_index()
wszystkie_lata_A = df.groupby(["Rok"])["Liczba"].sum().reset_index()
wszystkie_lata_K = wszystkie_lata[wszystkie_lata["Plec"] == "K"].reset_index()
wszystkie_lata_M = wszystkie_lata[wszystkie_lata["Plec"] == "M"].reset_index()

plt.bar(wszystkie_lata_K["Rok"], wszystkie_lata_A["Liczba"], label="Dziewczynki")
plt.bar(wszystkie_lata_M["Rok"], wszystkie_lata_M["Liczba"], label="Chłopcy")
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.title("Ilość narodzin dziewczynek i chłopców")
plt.legend()
plt.show()