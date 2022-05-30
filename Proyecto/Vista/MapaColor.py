import tkinter as tk
from tkinter import ttk


class MapaColorFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.titulo = tk.Label(self, text="Mapa de color", fg="white")
        self.titulo.pack()
