import tkinter as tk

window=tk.Tk()

WIDTH=HEIGHT=500

screnn_width=window.winfo_screenwidth()
screnn_height=window.winfo_screenheight()

print("Ecranul are width:", screnn_width, "Height:", screnn_height )

X=screnn_width // 2 - WIDTH // 2
Y=screnn_height // 2 - HEIGHT // 2

window.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

counter = 0
def aduna_valoare(val):
    global counter
    counter += val
    print("Counter", counter)
    counter_label.config(text=f"{counter}")

frame=tk.Frame(window)
frame.pack()

minus_button = tk.Button(frame,text="-", command= lambda x = -1:aduna_valoare(x))
minus_button.grid(row=0,column=0)

counter_label = tk.Label(frame,text =f"{counter}")
counter_label.grid(row=0, column =1)

plus_button = tk.Button(frame,text="+", command= lambda x = 1:aduna_valoare(x))
plus_button.grid(row=0,column=2)

label = tk.Label(window, text="Label-ul meu din fereastra mea")
label.pack()


window.mainloop()