from Tecnologia import Tecnologia

class Tvs(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamaño):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__tamaño = tamaño

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        return f"Marca: {self.__marca}\nVoltaje: {self.__voltaje}\nEficiencia: {self.__eficiencia}\nPrecio: ${self.__precio}\nTamaño: {self.__tamaño} pulgadas\nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:}"