class Imagen:
    def _init_(self):
        self.coberturaA4: float = 0.0
        self.costoA4: float = 0.0
        self.precioA4: int = 0
        self.coberturaA5: float = 0.0
        self.costoA5: float = 0.0
        self.precioA5: int = 0

    def _del_(self):
        print("")

    def calcular_precio_imagenA4(self, config):
        self.costoA4 = self.coberturaA4 * getattr(config,'costo_final_full') / 100
        #print(self.costoA4)
        precio = self.costoA4 * getattr(config, 'ganancia')
        self.precioA4 = int(precio)

    def calcular_precio_imagenA5(self, config):
        self.costoA5 = self.coberturaA5 * getattr(config,'costo_final_full') / 100
        #print(self.costoA5)
        precio = self.costoA5 * getattr(config, 'ganancia')
        self.precioA5 = int(precio)
