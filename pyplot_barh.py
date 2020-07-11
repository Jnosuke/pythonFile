import matplotlib.pyplot as plt
labels = list("ABCDE")
y_pos = range(0, 5)
V = [91, 45, 17, 88, 47]
plt.barh(y_pos, V, tick_label = labels)
plt.show() 
