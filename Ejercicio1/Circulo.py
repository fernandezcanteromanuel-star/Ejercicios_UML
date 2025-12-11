import math

class Circulo:
    def __init__(self, diametro, color):
        self.diametro = diametro
        self.color = color
    
    def get_diametro(self):
        return self.diametro
    
    def set_diametro(self, diametro):
        self.diametro = diametro
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def calcular_area(self):
        radio = self.diametro / 2
        return math.pi * radio ** 2
    
    def calcular_perimetro(self):
        return math.pi * self.diametro
