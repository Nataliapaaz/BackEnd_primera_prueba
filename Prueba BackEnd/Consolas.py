from Tecnologia import Tecnologia

class Consolas(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version, lite=False):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__nombre = nombre
        self.__version = version
        self.__lite = lite

    def calcular_descuento(self):
        descuento_eficiencia = super().calcular_descuento()
        if self.__lite:
            return descuento_eficiencia + 0.05
        else:
            return descuento_eficiencia
        
    def mostrar_caracteristicas(self):
        print(f"Marca: {self.__marca}")
        print(f"Voltaje: {self.__voltaje}")
        print(f"Eficiencia: {self.__eficiencia}")
        print(f"Precio: ${self.__precio}")
        print(f"Nombre: {self.__nombre}")
        print(f"Versión: {self.__version}")
        descuento_eficiencia = self.calcular_descuento()
        precio_total = self.obtener_precio_total()
        print(f"Descuento aplicado: {descuento_eficiencia * 100}%")
        print(f"Valor total después del descuento: ${precio_total}")

# def cotizar(self):
#        descuento_eficiencia = self.calcular_descuento()
#       precio_con_descuento = self.precio * (1 - descuento_eficiencia)
#        return f"Marca: {self.marca}\nVoltaje: {self.voltaje}\nEficiencia: {self.# #   #eficiencia}\nPrecio: ${self.precio}\nNombre: {self.nombre}\nVersión: {self.version}#\nLite: {'Sí' if self.lite else 'No'}\nDescuento aplicado: {descuento_eficiencia * 100}#%\nPrecio total: ${precio_con_descuento:}"