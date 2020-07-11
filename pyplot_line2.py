import matplotlib.pyplot as plt
X = [100, 200, 300, 400, 500,]
Y1 = [40, 60, 50, 80, 42]
Y2 = [32, 48, 55, 60, 47]
Y3 = [11, 15,  90, 54, 63]
Y4 = [24, 78, 36, 85, 22]
plt.plot(X, Y1, marker="o", color="blue", linestyle = "-")
plt.plot(X, Y2, marker="v", color="red", linestyle = "--")
plt.plot(X, Y3, marker="^", color="green", linestyle = "-.")
plt.plot(X, Y4, marker="1", color="m", linestyle = ":")
plt.show()
