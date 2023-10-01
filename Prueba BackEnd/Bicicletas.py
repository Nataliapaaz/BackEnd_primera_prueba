from Transporte import Transporte

class Bicicletas(Transporte):
    def __init__(self, aro, peso, precio, marca):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def get_precio(self):
        return self.__precio

    def calcular_costo_despacho(self, precio):
        return 4000 + self.__peso * self.__precio
    
    def cotizar(self):
        precio = self.get_precio() + calcul
        return precio + self.__peso * precio

    def __str__(self):
        return f'Aro: {self.__aro} \n Peso: {self.__peso} \n Precio: {self.__precio} \n Marca: {self.__marca}'