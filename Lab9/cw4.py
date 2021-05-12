import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"])

iris_setosa = df[df["Species"]=="Iris-setosa"]
iris_versicolor = df[df["Species"]=="Iris-versicolor"]
iris_virginica = df[df["Species"]=="Iris-virginica"]

x = iris_setosa["SepalLengthCm"]
y = iris_setosa["PetalLengthCm"]
plt.scatter(x, y, color="r", label="I. setosa")

x2 = iris_versicolor["SepalLengthCm"]
y2 = iris_versicolor["PetalLengthCm"]
plt.scatter(x2, y2, color="y", label="I. versicolor")

x3 = iris_virginica["SepalLengthCm"]
y3 = iris_virginica["PetalLengthCm"]
plt.scatter(x3, y3, color="b", label="I. virginica")

plt.xlabel("Sepal length (cm)")
plt.ylabel("Petal length (cm)")
plt.title("Iris dataset: petal length vs sepal length")
plt.legend(loc="lower right")
plt.plot()
plt.show()