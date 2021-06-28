import tkinter as tk
import pypokedex
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO


window = tk.Tk()
window.geometry("600x500")
window.title("My First App")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="My Pokedex")
title_label.config(font=("Arial",20), padx=10, pady=10)
title_label.pack()

pokemon_image = tk.Label(window)
pokemon_image.config(font=("Arial",20))
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial",20),padx=10,pady=10)
pokemon_information.pack()

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20),padx=10,pady=10)
pokemon_types.pack()

label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("Arial", 20),padx=10,pady=10)
label_id_name.pack()

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20),padx=1, pady=1)
text_id_name.pack()


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0,"end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))

    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")


btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20),padx=1, pady=1)
btn_load.pack()


def call():
    window.mainloop()

if __name__ == "__main__":
    call()