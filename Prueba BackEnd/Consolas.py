from Tecnologia import Tecnologia

class Consolas(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version, lite=False):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__nombre = nombre
        self.__version = version
        self.__lite = lite

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_version(self):
        return self.__version
    
    def set_version(self, version):
        self.__version = version

    def get_lite(self):
        return self.__lite
    
    def set_lite(self, lite):
        self.__lite = lite

    def calcular_descuento(self):
        descuento_eficiencia = super().calcular_descuento()
        if self.__lite:
            return descuento_eficiencia + 0.05
        else:
            return descuento_eficiencia
        
    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.get_precio() * (1 - descuento_eficiencia)
        return f"Nombre: {self.get_nombre()}\nVoltaje: {self.get_voltaje()}\nEficiencia: {self.get_eficiencia()}\nPrecio: ${self.get_precio()}\nVersion: {self.get_version()} \nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:}"
        
    def __str__(self):
        return f'{super().__str__()} \n Nombre: {self.__nombre} \n Version: {self.__version} \n Lite {self.__lite}'