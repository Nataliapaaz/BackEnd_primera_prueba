class Bicicletas:
    def __init__(self, aro, peso, precio, marca):
        self.aro = aro
        self.peso = peso
        self.precio = precio
        self.marca = marca

    def calcular_costo_despacho(self, precio):
        return 4000 + self.peso * precio
