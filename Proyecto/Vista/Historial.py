import tkinter as tk
from tkinter import ttk


class HistorialFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.titulo = tk.Label(self, text="Hitorial", fg="white")
        self.titulo.pack()

        self.historial = tk.Text(self)
        self.historial.pack()

        #self.atrapa_texto()

    # def atrapa_texto(self):
    #     f = open('prueba.txt', 'r')
    #     mensaje = f.read()
    #     f.close()
    #     self.historial.insert(1.0, mensaje)
