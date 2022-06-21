import os


class Config:
    def __init__(self):
        self.costoTinta: float = 0.0
        self.costoPapel: float = 0.0
        self.servicioTecnico: float = 0.0
        self.ganancia: float = 0.0
        self.costo_final_full: float = 0.0
        self.precio_final_full: float = 0.0

    def set_valores_iniciales(self):
        config = get_config()
        self.costoTinta = float(config[0])
        self.costoPapel = float(config[1])
        self.servicioTecnico = float(config[2])
        self.ganancia = float(config[3])
        self.costo_final_full = ((self.costoTinta * 4) + (self.costoPapel * 2) + self.servicioTecnico) / 1000
        self.precio_final_full = self.costo_final_full * self.ganancia


def set_valores_reset():
    valor_inicial= '1;1;1;1'
    guardar_config(valor_inicial)



def guardar_config(datos):
    fichero = open(
        os.path.dirname(__file__).replace("Modelo", "Historial") + "/config.txt",
        'w')
    fichero.write(datos)
    fichero.close()


def get_config():
    f = open(
        os.path.dirname(__file__).replace("Modelo", "Historial") + "/config.txt",
        'r')
    text = f.read()
    f.close()
    config = text.split(';')
    return config
