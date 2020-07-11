import matplotlib.pyplot as plt
from random import randint

X1 = []
Y1 = []
X2 = []
Y2 = []
for i in range(55):
    X1.append(randint(1, 100))
    Y1.append(randint(1, 60))
    X2.append(randint(1, 100))
    Y2.append(randint(1, 60))

plt.scatter(X1, Y1, marker="+", color = "red")
plt.scatter(X2, Y2, marker="^", color = "green")

plt.show()
