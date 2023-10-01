from Tecnologia import Tecnologia

class Consolas(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version, lite=False):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.nombre = nombre
        self.version = version
        self.lite = lite

    def calcular_descuento(self):
        descuento_eficiencia = super().calcular_descuento()
        if self.lite:
            descuento_eficiencia += 0.05
        return min(descuento_eficiencia, 1.0)

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        return f"Marca: {self.marca}\nVoltaje: {self.voltaje}\nEficiencia: {self.eficiencia}\nPrecio: ${self.precio}\nNombre: {self.nombre}\nVersión: {self.version}\nLite: {'Sí' if self.lite else 'No'}\nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:.2f}"