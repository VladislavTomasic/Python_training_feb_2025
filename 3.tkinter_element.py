import tkinter as tk

window=tk.Tk()

WIDTH=HEIGHT=500

screnn_width=window.winfo_screenwidth()
screnn_height=window.winfo_screenheight()

print("Ecranul are width:", screnn_width, "Height:", screnn_height )

X=screnn_width // 2 - WIDTH // 2
Y=screnn_height // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")


label = tk.Label(window, text="Label-ul meu din fereastra mea")
label.pack()

label2 = tk.Label(window, text="Alt label-ul meu din fereastra mea")
label2.pack()


label_list =[]
for i in range(100):
    newlabel = tk.Label(window, text=f"Label-ul meu din fereastra mea numar {i}")
    newlabel.pack()

# window.resizable(False,False)

scroll_bar = tk.Scrollbar(window)
scroll_bar.pack()

window.mainloop()