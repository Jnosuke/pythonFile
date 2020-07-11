import tkinter as tk
import tkinter.filedialog as fd
from random import random

def getdata():
    num = random()
    return str(num)

root = tk.Tk()
root.withdraw()
file = fd.asksaveasfilename(
    initialfile = "mydata",
    defaultextension = ".txt",
    title = "保存場所を選んでください。",
    filetypes = [("TEXT", ".txt")]
)

savedata = getdata()
if file:
    with open(file, "w", encoding="utf-8") as fileobj:
        len = fileobj.write(savedata)
        print(f"{len}文字保存しました。")
