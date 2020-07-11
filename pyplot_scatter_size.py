import matplotlib.pyplot  as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)
V = np.random.rand(100)*1000 + 50
plt.scatter(X, Y, marker = "o", s = V, color = "b", alpha = 0.3,
    linewidths = 1, edgecolors = "b")
plt.show()
