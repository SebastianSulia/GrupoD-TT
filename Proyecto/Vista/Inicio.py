import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class InicioFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.titulo = tk.Label(self, text="Calculo de porcentaje de color", fg="white")
        self.titulo.pack(pady=3)
        # -----------------------------
        self.url = tk.Entry(self)
        self.url.pack(pady=2)
        # -----------------------------
        self.boton_buscar = tk.Button(self, text="Buscar", command=self.buscar)
        self.boton_buscar.pack(pady=2)
        # -----------------------------
        self.boton_ejecutar= tk.Button(self, text="Ejecutar", command=self.ejecutar)
        self.boton_ejecutar.pack(pady=2)

    def buscar(self):
        archivo = filedialog.askopenfilename(title="Buscar")
        self.url.insert(0, archivo)
        print(archivo)

    def ejecutar(self):
        print(self.url.get())
