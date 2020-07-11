import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
root.withdraw()

file = fd.askopenfilename(
    title = "ファイルを選んでください。",
    filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

if file:
    with open(file, "r", encoding="utf-8") as fileobj:
        text = fileobj.read()
        print(text)
