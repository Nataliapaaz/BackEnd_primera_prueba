class Bicicleta:
    def __init__(self, aro:float, peso:float, precio:float, marca:str):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def aro(self):
        return self.__aro
    
    def peso(self):
        return self.__peso
    
    def precio(self):
        return self.__precio
    
    def marca(self):
        return self.__marca