import math

class Elipse:
    def __init__(self, eje_mayor, eje_menor, color):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color
    
    def get_eje_mayor(self):
        return self.eje_mayor
    
    def set_eje_mayor(self, eje_mayor):
        self.eje_mayor = eje_mayor
    
    def get_eje_menor(self):
        return self.eje_menor
    
    def set_eje_menor(self, eje_menor):
        self.eje_menor = eje_menor
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def calcular_area(self):
        return math.pi * (self.eje_mayor / 2) * (self.eje_menor / 2)
    