import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

rok = df.groupby("Rok")["Liczba"].sum()
chart = rok.plot(color="g")
chart.set_ylabel('Liczba urodzeń')
plt.title("dzieci")
plt.show()