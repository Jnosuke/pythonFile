import matplotlib.pyplot as plt
from random import randint

X = []
Y = []
for i in range(55):
    X.append(randint(1, 100))
    Y.append(randint(1, 60))

plt.scatter(X, Y)
plt.show()
