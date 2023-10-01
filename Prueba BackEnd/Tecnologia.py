class Tecnologia:
    def __init__(self, marca, voltaje, eficiencia, precio):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__eficiencia = eficiencia
        self.__precio = precio

    def calcular_descuento(self):
        if self.__eficiencia in ['A', 'B']:
            return 0.5
        elif self.__eficiencia in ['C', 'D']:
            return 0.3
        elif self.__eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def obtener_precio_total(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_descuento = self.__precio - (self.__precio * descuento_eficiencia)
        return precio_descuento
    
    def __str__(self):
        return f"Información de Producto Tecnológico:\n Marca: {self.__marca} \n Voltaje: {self.__voltaje} \n Eficiencia: {self.__eficiencia}\n Precio: ${self.__precio:}\n descuento_eficiencia = {self.calcular_descuento()}\n Descuento aplicado: {self.obtener_precio_total()}"
