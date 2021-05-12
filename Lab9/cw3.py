import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

rok = df[((df.Rok <= 2017) & (df.Rok >= 2013))]
rok = rok.groupby("Plec")["Liczba"].sum()
wykres = rok.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title(" proc. chłopców i dziewczynek w ostatnich 5 latach")
plt.show()