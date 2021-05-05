import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

#A
imie = df[df["Liczba"]>1000]
print(imie)

#B
patryk = df[df["Imie"]=="PATRYK"]
print(patryk)

#C
print(df["Liczba"].sum())

#D
df_sum = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print(df_sum.groupby("Rok")["Liczba"].sum())

#E
print(df.groupby("Plec")["Liczba"].sum())

#F
a = df.loc[df.groupby(["Rok", "Plec"])["Liczba"].idxmax()]
print(a.drop(["Liczba", "Plec"], axis=1))

#G
a = df.loc[df.groupby(["Plec"])["Liczba"].idxmax()]
print(a.drop(["Liczba", "Plec"], axis=1))