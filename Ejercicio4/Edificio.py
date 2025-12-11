class Edificio:
    def __init__(self, nombre, tipo, ubicacion, ciudad, provincia, pais):
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
        self.fecha_inicio = None
        self.fecha_fin = None
        self.material_principal = None
        self.estilos_arquitectonicos = []
        self.fecha_consagracion = None
        self.fecha_ultima_consagracion = None
        self.proteccion_legal = None
        self.fecha_proteccion = None
    
    def nombre_edificio(self):
        return self.nombre
    
    def tipo_construccion(self):
        return self.tipo
    
    def localizacion(self):
        return f"{self.ubicacion}, {self.ciudad}, {self.provincia} ({self.pais})"
    
    def iniciar_construccion(self, año):
        self.fecha_inicio = año
    
    def terminar_construccion(self, año):
        self.fecha_fin = año
    
    def periodo_construccion(self):
        return f"{self.fecha_inicio} - {self.fecha_fin}"
    
    def material_construccion(self, material):
        self.material_principal = material
    
    def material(self):
        return self.material_principal
    
    def agregar_estilo(self, estilo):
        self.estilos_arquitectonicos.append(estilo)
    
    def estilos(self):
        return ", ".join(self.estilos_arquitectonicos)
    
    def consagrar(self, año):
        self.fecha_consagracion = año
    
    def fecha_primera_consagracion(self):
        return self.fecha_consagracion
    
    def consagracion_definitiva(self, año):
        self.fecha_ultima_consagracion = año
    
    def fecha_consagracion_final(self):
        return self.fecha_ultima_consagracion
    
    def declarar_proteccion(self, tipo_proteccion, año):
        self.proteccion_legal = tipo_proteccion
        self.fecha_proteccion = año
    
    def proteccion(self):
        return self.proteccion_legal
    
    def año_proteccion(self):
        return self.fecha_proteccion
    
    def __str__(self):
        return f"{self.nombre} - {self.tipo}"
