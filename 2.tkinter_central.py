import tkinter as tk

window=tk.Tk()

WIDTH=HEIGHT=500

screnn_width=window.winfo_screenwidth()
screnn_height=window.winfo_screenheight()

print("Ecranul are width:", screnn_width, "Height:", screnn_height )

X=screnn_width // 2 - WIDTH // 2
Y=screnn_height // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

window.mainloop()