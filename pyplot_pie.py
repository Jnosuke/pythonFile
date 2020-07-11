import matplotlib.pyplot as plt
labels = list("ABCDE")
V = [17, 25, 47, 68, 91]
ex = [0.1, 0.1, 0.1, 0.1, 0.1]
plt.pie(V, explode=ex, labels=labels, autopct="%1.1f%%", startangle=90, counterclock=False)
plt.show()
