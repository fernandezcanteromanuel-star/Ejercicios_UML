class Rectangulo:
    def __init__(self, longitud, anchura, color):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    def get_longitud(self):
        return self.longitud
    
    def set_longitud(self, longitud):
        self.longitud = longitud
    
    def get_anchura(self):
        return self.anchura
    
    def set_anchura(self, anchura):
        self.anchura = anchura
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def calcular_area(self):
        return self.longitud * self.anchura
    
    def calcular_perimetro(self):
        return 2 * (self.longitud + self.anchura)
