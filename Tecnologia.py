class Tecnologia:
    def __init__(self, voltaje:int, precio:float, eficiencia:str, marca:str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def voltaje(self):
        return self.__voltaje
    
    def precio(self):
        return self.__precio
    
    def eficiencia(self):
        return self.__eficiencia
    
    def marca(self):
        return self.__marca
    
    def mostrar(self):
        return "Producto\n"+"Voltaje:"+self.__voltaje+" - Precio:"+str(self.__precio)
