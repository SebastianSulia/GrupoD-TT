import tkinter as tk
from tkinter import ttk

from Vista.Config import ConfigFrame
from Vista.Historial import HistorialFrame
from Vista.Inicio import InicioFrame
from Vista.MapaColor import MapaColorFrame


class Principal(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Calculadora de color")

        self.notebook = ttk.Notebook(self)

        self.inicio = InicioFrame(self.notebook)
        self.notebook.add(self.inicio, text="Calculadora", padding=10)

        self.config = ConfigFrame(self.notebook)
        self.notebook.add(self.config, text="Configuracion", padding=10)

        self.historial = HistorialFrame(self.notebook)
        self.notebook.add(self.historial, text="Historial", padding=10)

        self.mapa_color = MapaColorFrame(self.notebook)
        self.notebook.add(self.mapa_color, text="Mapa de color", padding=10)

        self.notebook.pack(padx=10, pady=10)
        self.pack()
