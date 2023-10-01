class Transporte:
    def __init__(self, peso, despacho):
        self.__peso = peso
        self.__desepacho = 4000

    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

    def get_desepacho(self):
        return self.__desepacho