class Cuadrado:
    def __init__(self, longitud, color):
        self.longitud = longitud
        self.color = color
    
    def get_longitud(self):
        return self.longitud
    
    def set_longitud(self, longitud):
        self.longitud = longitud
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def calcular_area(self):
        return self.longitud ** 2
    
    def calcular_perimetro(self):
        return 4 * self.longitud
