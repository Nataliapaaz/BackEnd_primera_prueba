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
    
    def imprimir_informacion(self):
        print("Información de Producto Tecnológico:")
        print(f"Marca: {self.__marca}")
        print(f"Voltaje: {self.__voltaje}")
        print(f"Eficiencia: {self.__eficiencia}")
        print(f"Precio: ${self.__precio:}")
        descuento_eficiencia = self.calcular_descuento()
        print(f"Descuento aplicado: {descuento_eficiencia * 100}%")
        precio_con_descuento = self.__precio * (1 - descuento_eficiencia)
        print(f"Precio total: ${precio_con_descuento:}")
