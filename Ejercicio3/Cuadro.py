class Cuadro:
    def __init__(self, titulo, autor, fecha_inicio, fecha_fin, tecnica, subtecnica, material_soporte, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material_soporte = material_soporte
        self.descripcion = descripcion
        self.museo = None
        self.original = None
    
    def titulo_obra(self):
        return self.titulo
    
    def creador(self):
        return self.autor
    
    def periodo(self):
        return f"{self.fecha_inicio} - {self.fecha_fin}"
    
    def metodo_pintura(self):
        return self.tecnica
    
    def detalles_tecnica(self):
        return self.subtecnica
    
    def soporte(self):
        return self.material_soporte
    
    def info(self):
        return self.descripcion
    
    def ubicacion(self, museo):
        self.museo = museo
    
    def donde_esta(self):
        return self.museo
    
    def es_copia_de(self, original):
        self.original = original
    
    def obra_original(self):
        return self.original
    
    def __str__(self):
        return f"{self.titulo} - Autor: {self.autor}"
