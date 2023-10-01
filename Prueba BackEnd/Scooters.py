from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooters(Transporte, Tecnologia):
    def __init__(self, peso, despacho,marca, voltaje, eficiencia, precio, velocidad) :
        super().__init__(peso, despacho)
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__velocidad = velocidad

    def get_velocidad(self):
        return self.__velocidad
    
    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.get_precio() * (1 - descuento_eficiencia)
        costo_despacho = self.calcular_costo_despacho(300) 
        precio_total = precio_con_descuento + costo_despacho
        return f"Marca: {self.get_marca()}\nVoltaje: {self.get_voltaje()}\nEficiencia: {self.get_eficiencia()}\nPrecio: ${self.get_precio()}\nPeso: {self.get_precio()}\nVelocidad: {self.get_velocidad()} km/h\n \nDescuento aplicado: {descuento_eficiencia * 100}%\nCosto de despacho: ${costo_despacho:}\nPrecio total: ${precio_total:}"
    
    def __str__(self):
        return f'{super().__str__()} \n Velocidad: {self.__velocidad}'