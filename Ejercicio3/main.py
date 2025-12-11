from Cuadro import Cuadro

if __name__ == '__main__':
    gioconda_original = Cuadro(
        "La Gioconda",
        "Leonardo Da Vinci",
        1503,
        1516,
        "óleo",
        "sfumato",
        "madera de álamo",
        "Obra maestra original de Leonardo Da Vinci"
    )
    gioconda_original.ubicacion("Museo Louvre (París)")
    
    gioconda_replica = Cuadro(
        "La Gioconda",
        "Anónimo (alumno de Leonardo)",
        1503,
        1516,
        "óleo",
        "pincelada simple",
        "madera de nogal",
        "Réplica contemporánea realizada por un alumno de Leonardo al mismo tiempo que el maestro pintaba la original"
    )
    gioconda_replica.ubicacion("Museo del Prado (Madrid)")
    gioconda_replica.es_copia_de(gioconda_original)
    
    print("=== DIAGRAMA DE OBJETOS ===\n")
    print(f"Objeto: Gioconda Original")
    print(f"  Título: {gioconda_original.titulo_obra()}")
    print(f"  Autor: {gioconda_original.creador()}")
    print(f"  Período: {gioconda_original.periodo()}")
    print(f"  Técnica: {gioconda_original.metodo_pintura()}")
    print(f"  Sub-técnica: {gioconda_original.detalles_tecnica()}")
    print(f"  Material: {gioconda_original.soporte()}")
    print(f"  Ubicación: {gioconda_original.donde_esta()}")
    print(f"  Descripción: {gioconda_original.info()}\n")
    
    print(f"Objeto: Gioconda Réplica")
    print(f"  Título: {gioconda_replica.titulo_obra()}")
    print(f"  Autor: {gioconda_replica.creador()}")
    print(f"  Período: {gioconda_replica.periodo()}")
    print(f"  Técnica: {gioconda_replica.metodo_pintura()}")
    print(f"  Sub-técnica: {gioconda_replica.detalles_tecnica()}")
    print(f"  Material: {gioconda_replica.soporte()}")
    print(f"  Ubicación: {gioconda_replica.donde_esta()}")
    print(f"  Original: {gioconda_replica.obra_original()}")
    print(f"  Descripción: {gioconda_replica.info()}\n")
