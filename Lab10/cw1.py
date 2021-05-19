import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1., 20.2, 0.2)
plt.plot(x, 1/x, label="f(x)=1/x")
plt.axis([1, 20, 0, 1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) = 1/x")
plt.legend()
plt.show()