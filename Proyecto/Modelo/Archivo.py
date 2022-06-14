
class Archivo:
    def __init__(self):
        self.paginas = []
        self.costo: float = 0.0
        self.precio: int = 0

    def add_pagina(self,pagina):
        getattr(self,'paginas',self.paginas.append(pagina))

    def calcular_precio_archivo(self, config):
        costo = 0
        for pag in self.paginas:
            costo += self.calcular_costo_pag(getattr(pag,'cobertura'), config)
            #print(costo)
        self.costo = costo
        precio = costo * getattr(config, 'ganancia')
        self.precio = int(precio)

    def calcular_costo_pag(self,cobertura_pag,config):
        costo_pag = cobertura_pag * getattr(config,'costo_final_full') / 100
        return costo_pag

    def resert_archivo(self):
        self.paginas = []
        self.costo = 0.0
        self.precio = 0
