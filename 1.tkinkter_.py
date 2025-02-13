import tkinter as tk

window=tk.Tk()

WIDTH=5000
HEIGHT=100
X=20
Y=30

window.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

window.mainloop()