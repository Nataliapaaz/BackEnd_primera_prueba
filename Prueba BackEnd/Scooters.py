from Tecnologia import Tecnologia
from Bicicletas import Bicicletas

class Scooters(Bicicletas, Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, aro, velocidad, peso):
        super().__init__(aro, peso, precio, marca)
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__velocidad = velocidad

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        costo_despacho = self.calcular_costo_despacho(300)  # Valor por kg para Scooter
        precio_total = precio_con_descuento + costo_despacho
        return f"Marca: {self.marca}\nVoltaje: {self.voltaje}\nEficiencia: {self.eficiencia}\nPrecio: ${self.precio}\nAro: {self.aro}\nVelocidad: {self.velocidad} km/h\nPeso: {self.peso} kg\nDescuento aplicado: {descuento_eficiencia * 100}%\nCosto de despacho: ${costo_despacho:}\nPrecio total: ${precio_total:}"