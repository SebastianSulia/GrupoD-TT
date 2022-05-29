from Modelo import Pagina


class Archivo:
    def __init__(self):
        self.paginas = []
        self.costo: float = 0.0
        self.precioCosto: int = 0

    def add_pagina(self, pagina):
        self.paginas.append(pagina)

    def set_costo(self, costo):
        self.costo = costo

    def set_precioCosto(self, precioCosto):
        self.precioCosto = precioCosto
