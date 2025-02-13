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


INCREMENT = 0
def printeaza_inconsola():
    global INCREMENT
    INCREMENT+=1
    print(f"Butonul apasat {INCREMENT}")



button=tk.Button(window,text="Apasa ma?",command=printeaza_inconsola)
button.pack()

window.mainloop()