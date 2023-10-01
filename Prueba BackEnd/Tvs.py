from Tecnologia import Tecnologia

class Tvs(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamaño):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.tamaño = tamaño

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        return f"Marca: {self.marca}\nVoltaje: {self.voltaje}\nEficiencia: {self.eficiencia}\nPrecio: ${self.precio}\nTamaño: {self.tamaño} pulgadas\nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:.2f}"