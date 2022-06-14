import os
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime

import Modelo.ArchivoService
from Modelo import *


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
        self.boton_ejecutar = tk.Button(self, text="Ejecutar", command=self.ejecutar)
        self.boton_ejecutar.pack(pady=2)
        # -----------------------------
        self.detalle = tk.Text(self, height=10, width=40)

    def buscar(self):
        archivo = filedialog.askopenfilename(title="Buscar")
        self.url.insert(0, archivo)
        self.detalle.pack_forget()

        self.borrar_detalle()
        #print(archivo)

    def ejecutar(self):
        #print(self.url.get())
        info = Modelo.ArchivoService.entrada_archivo(self.url.get())
        if(info != None):
            self.detalle.insert("insert", self.escribir_info(info))
            self.detalle.pack()
            self.guardar_en_historial(info)

        self.borrar_path()

    def escribir_info(self, info):
        if len(info) == 1:
            return info[0]

        if len(info) == 3:
            string = str(datetime.now().date()) + "\n" + "Nombre archivo: " + str(info[0]) + "\n" + "Numero de paginas: " + str(
                info[1]) + "\n" + "Precio: $" + str(info[2]) + "\n"
            return string

        elif len(info) == 5:
            string = str(datetime.now().date()) + "\n" + "Nombre archivo: " + str(info[0]) + "\n" + str(
                info[1]) + "\n" + "$" + str(info[2]) + "\n" + str(
                info[3]) + "\n" + "$" + str(info[4])
            return string

    def borrar_path(self):
        self.url.delete(0, tk.END)

    def borrar_detalle(self):
        self.detalle.delete(1.0, tk.END)

    def guardar_en_historial(self, info):
        fichero = open(
            os.path.dirname(__file__).replace("Vista", "Historial") + "/history.txt",
            'a')
        fichero.write(self.escribir_info(info) + '\n')
        fichero.close()
