from Tecnologia import Tecnologia

class Tvs(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamaño):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__tamaño = tamaño

    def get_tamaño(self):
        return self.__tamaño
    
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.get_precio() * (1 - descuento_eficiencia)
        return f"Marca: {self.get_precio()}\nVoltaje: {self.get_voltaje()}\nEficiencia: {self.get_eficiencia()}\nPrecio: ${self.get_precio()}\nTamaño: {self.get_tamaño()} pulgadas\nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:}"
    
    def __str__(self):
        return f'{super().__str__()} \n Tamaño {self.__tamaño}'
    