from Transporte import Transporte

class Bicicletas(Transporte):
    def __init__(self, aro, peso, precio, marca):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def calcular_descuento(self):
        if self.eficiencia in ['A', 'B']:
            return 0.5
        elif self.eficiencia in ['C', 'D']:
            return 0.3
        elif self.eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def calcular_costo_despacho(self, precio):
        return 4000 + self.__peso * precio

