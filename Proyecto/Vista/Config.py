import tkinter as tk
from tkinter import ttk
from Modelo import Config


class ConfigFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.titulo = tk.Label(self, text="Configuracion", fg="white")
        self.titulo.grid(row=1, column=2)

        self.costo_tinta = tk.Label(self, text="Costo tinta", fg="white")
        self.costo_tinta.grid(row=2, column=1)
        self.costo_tinta_entry = tk.Entry(self)
        self.costo_tinta_entry.grid(row=2, column=2)

        self.costo_papel = tk.Label(self, text="Costo papel", fg="white")
        self.costo_papel.grid(row=3, column=1)
        self.costo_papel_entry = tk.Entry(self)
        self.costo_papel_entry.grid(row=3, column=2)

        self.servicio_tecnico = tk.Label(self, text="Servicio Tecnico", fg="white")
        self.servicio_tecnico.grid(row=4, column=1)
        self.servicio_tecnico_entry = tk.Entry(self)
        self.servicio_tecnico_entry.grid(row=4, column=2)

        self.ganancia = tk.Label(self, text="Ganancia", fg="white")
        self.ganancia.grid(row=5, column=1)
        self.ganancia_entry = tk.Entry(self)
        self.ganancia_entry.grid(row=5, column=2)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.configurar)
        self.boton_guardar.grid(row=6, column=1)

        self.boton_reset = tk.Button(self, text="Predeterminado", command=self.reset)
        self.boton_reset.grid(row=6, column=2, sticky="e")

        self.mostrar_valores()

    def mostrar_valores(self):
        config = Config.Config()
        config.set_valores_iniciales()

        self.vaciar_valores()

        self.costo_tinta_entry.insert(0, str(config.costoTinta))
        self.costo_papel_entry.insert(0, str(config.costoPapel))
        self.servicio_tecnico_entry.insert(0, str(config.servicioTecnico))
        self.ganancia_entry.insert(0, str(config.ganancia))

    def vaciar_valores(self):
        self.costo_tinta_entry.delete(0, tk.END)
        self.costo_papel_entry.delete(0, tk.END)
        self.servicio_tecnico_entry.delete(0, tk.END)
        self.ganancia_entry.delete(0, tk.END)

    def reset(self):
        Config.set_valores_reset()
        self.mostrar_valores()

    def configurar(self):
        Config.guardar_config(self.get_valores())

    def get_valores(self):
        return str(self.costo_tinta_entry.get()) + ';' + str(self.costo_papel_entry.get()) + ';' + str(
            self.servicio_tecnico_entry.get()) + ';' + str(self.ganancia_entry.get())
