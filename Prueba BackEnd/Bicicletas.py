from Transporte import Transporte

class Bicicletas(Transporte):
    def __init__(self, aro, peso, precio, marca, despacho):
        super().__init__(peso, despacho)
        self.__aro = aro
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

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca

    def calcular_costo_despacho(self):
        return 4000 + self.get_peso() * self.get_precio()
    
    def cotizar(self):
        precio = self.get_precio() + self.calcular_costo_despacho()
        return f'Precio: {precio}'

    def __str__(self):
        return f'{super().__str__()} \n Precio {self.__precio}\n Aro: {self.__aro} \n Marca {self.__marca}'