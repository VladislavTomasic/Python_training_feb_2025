import tkinter as tk
import requests
import json

window = tk.Tk()
# Create and pack an input entry
input_entry = tk.Entry(window)
input_entry.pack()

joke_label = tk.Label(window, text="Aici va fi gluma....")
joke_label.pack()

# lucru cu API
def fetch_new_joke():
    LINK = "https://api.chucknorris.io/jokes/search"
    parametri = {"Accept": "application/json"}

    search_term = input_entry.get()

    response = requests.get(LINK, headers=parametri, params={"query": search_term})
    json_response = json.loads(response.text)
    print(json_response)
    results = json_response['result']
    if results:
        joke = results[0]['value']
        joke_label.config(text=joke)
    else:
        joke_label.config(text="Nicio glumă nu a fost găsită.")

fetch_button = tk.Button(window, text="Încearcă o glumă nouă", command=fetch_new_joke)
fetch_button.pack()

window.mainloop()
