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

minus_button = tk.Button(window,text="-", command= lambda x = -1:aduna_valoare(x))
minus_button.grid(row=0,column=0)


counter_label = tk.Label(window,text =f"{counter}")
counter_label.grid(row=0, column =1)

plus_button = tk.Button(window,text="+", command= lambda x = 1:aduna_valoare(x))
plus_button.grid(row=0,column=2)


# label = tk.Label(window, text="Label-ul meu din fereastra mea")
# label.pack()

# label2 = tk.Label(window, text="Alt label-ul meu din fereastra mea")
# label2.pack()


# INCREMENT = 0
# def printeaza_inconsola():
#     global INCREMENT
#     INCREMENT+=1
#     print(f"Butonul apasat {INCREMENT}")



# button=tk.Button(window,text="Apasa ma?",command=printeaza_inconsola)
# button.pack()

window.mainloop()