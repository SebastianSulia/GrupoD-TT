class Config:
    def __init__(self):
        self.costoTinta: float = 0.0
        self.costoPapel: float = 0.0
        self.servicioTecnico: float = 0.0
        self.ganancia: float = 0.0
        self.costo_final_full: float = 0.0
        self.precio_final_full: float = 0.0

    def set_valores_iniciales(self):
        self.costoTinta = 1500
        self.costoPapel = 650
        self.servicioTecnico = 8000
        self.ganancia = 3.3
        self.costo_final_full = ((self.costoTinta*4)+(self.costoPapel*2)+self.servicioTecnico)/1000
        self.precio_final_full = self.costo_final_full * self.ganancia
