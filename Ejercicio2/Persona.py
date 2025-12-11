class Persona:
    def __init__(self, nombre, apellido_nacimiento, apellido_actual):
        self.nombre = nombre
        self.apellido_nacimiento = apellido_nacimiento
        self.apellido_actual = apellido_actual
        self.pareja = None
        self.padre = None
        self.madre = None
    
    def nombre_completo(self):
        return self.nombre
    
    def apellido_origen(self):
        return self.apellido_nacimiento
    
    def apellido(self):
        return self.apellido_actual
    
    def casarse(self, pareja):
        self.pareja = pareja
    
    def obtener_pareja(self):
        return self.pareja
    
    def agregar_padre(self, padre):
        self.padre = padre
    
    def obtener_padre(self):
        return self.padre
    
    def agregar_madre(self, madre):
        self.madre = madre
    
    def obtener_madre(self):
        return self.madre
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_actual} (nacida/o {self.apellido_nacimiento})"
