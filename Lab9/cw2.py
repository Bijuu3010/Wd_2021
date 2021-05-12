import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

liczba = df.groupby("Plec")["Liczba"].sum()
chart = liczba.plot.bar()
chart.set_ylabel('Liczba urodzeń')
chart.set_xlabel('Płeć')
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()