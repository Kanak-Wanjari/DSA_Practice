import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

X = np.linspace(-3, 3, 50)
y = X**2 + np.random.randn(50) * 2

coeffs = np.polyfit(X, y, deg=3)
y_pred = np.polyval(coeffs, X)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title("Balanced Bias–Variance")
plt.show()