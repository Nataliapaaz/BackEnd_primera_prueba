from Transporte import Transporte

class Bicicletas(Transporte):
    def __init__(self, aro, peso, precio, marca):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

    def get_aro(self):
        return self.__aro
    
    def set_aro(self, aro):
        self.__aro = aro

    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca

    def calcular_costo_despacho(self, precio):
        return 4000 + self.__peso * self.__precio
    
    def cotizar(self):
        precio = self.get_precio() + self.calcular_costo_despacho()
        return precio

    def __str__(self):
        return f'Aro: {self.__aro} \n Peso: {self.__peso} \n Precio: {self.__precio} \n Marca: {self.__marca}'