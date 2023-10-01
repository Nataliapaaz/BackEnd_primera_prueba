class Tecnologia:
    def __init__(self, marca, voltaje, eficiencia, precio):
        self.marca = marca
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.precio = precio

    def calcular_descuento(self):
        if self.eficiencia in ['A', 'B']:
            return 0.5
        elif self.eficiencia in ['C', 'D']:
            return 0.3
        elif self.eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0
        
    def cotizar(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        return f"Marca: {self.marca}\nVoltaje: {self.voltaje}\nEficiencia: {self.eficiencia}\nPrecio: ${self.precio}\nDescuento aplicado: {descuento_eficiencia * 100}%\nPrecio total: ${precio_con_descuento:}"
    
    def imprimir_informacion(self):
        print("Información de Producto Tecnológico:")
        print(f"Marca: {self.marca}")
        print(f"Voltaje: {self.voltaje}")
        print(f"Eficiencia: {self.eficiencia}")
        print(f"Precio: ${self.precio:}")
        descuento_eficiencia = self.calcular_descuento()
        print(f"Descuento aplicado: {descuento_eficiencia * 100}%")
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        print(f"Precio total: ${precio_con_descuento:}")
