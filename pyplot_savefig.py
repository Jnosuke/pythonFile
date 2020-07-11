import matplotlib.pyplot as plt
import math
import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
root.withdraw()

file = fd.asksaveasfilename(
    initialfile = "sin",
    defaultextension = ".png",
    title = "保存場所を選んでください",
    filetypes=[("PICTER", ".png")]
)

X = range(0, 360)
Y = [math.sin(math.radians(d)) for d in X]
plt.plot(X, Y)
plt.savefig(file)
plt.show()
