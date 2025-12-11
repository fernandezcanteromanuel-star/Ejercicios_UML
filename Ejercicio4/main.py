from Edificio import Edificio

if __name__ == '__main__':
    catedral = Edificio(
        "Catedral de Santiago de Compostela",
        "Templo de culto católico",
        "Centro de la provincia",
        "Santiago de Compostela",
        "La Coruña",
        "España"
    )
    
    catedral.iniciar_construccion(1075)
    catedral.terminar_construccion(1122)
    catedral.material_construccion("granito")
    
    catedral.consagrar(1128)
    
    catedral.agregar_estilo("románico")
    catedral.agregar_estilo("gótico")
    catedral.agregar_estilo("barroco")
    catedral.agregar_estilo("plateresco")
    catedral.agregar_estilo("neoclásico")
    
    catedral.consagracion_definitiva(1211)
    catedral.declarar_proteccion("Bien de Interés Cultural", 1896)
    
    print("=== DIAGRAMA DE OBJETOS ===\n")
    print(f"Objeto: {catedral.nombre_edificio()}")
    print(f"  Tipo: {catedral.tipo_construccion()}")
    print(f"  Ubicación: {catedral.localizacion()}")
    print(f"  Período de construcción: {catedral.periodo_construccion()}")
    print(f"  Material: {catedral.material()}")
    print(f"  Primera consagración: {catedral.fecha_primera_consagracion()}")
    print(f"  Consagración definitiva: 3 de abril de {catedral.fecha_consagracion_final()}")
    print(f"  Estilos arquitectónicos: {catedral.estilos()}")
    print(f"  Protección legal: {catedral.proteccion()}")
    print(f"  Año de protección: {catedral.año_proteccion()}\n")
