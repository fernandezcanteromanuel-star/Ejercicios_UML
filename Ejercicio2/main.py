from Persona import Persona

if __name__ == '__main__':
    diana = Persona("Diana", "Spencer", "Gales")
    carlos = Persona("Carlos", "Windsor", "Windsor")
    guillermo = Persona("Guillermo", "Windsor", "Gales")
    kate = Persona("Kate", "Middleton", "Windsor")
    
    guillermo.agregar_padre(carlos)
    guillermo.agregar_madre(diana)
    
    guillermo.casarse(kate)
    kate.casarse(guillermo)
    
    print("=== DIAGRAMA DE OBJETOS ===\n")
    print(f"Objeto: Diana\n  Nombre: {diana.nombre_completo()}\n  Apellido actual: {diana.apellido()}\n  Apellido nacimiento: {diana.apellido_origen()}\n")
    
    print(f"Objeto: Carlos\n  Nombre: {carlos.nombre_completo()}\n  Apellido actual: {carlos.apellido()}\n  Apellido nacimiento: {carlos.apellido_origen()}\n")
    
    print(f"Objeto: Guillermo\n  Nombre: {guillermo.nombre_completo()}\n  Apellido actual: {guillermo.apellido()}\n  Apellido nacimiento: {guillermo.apellido_origen()}\n  Padre: {guillermo.obtener_padre()}\n  Madre: {guillermo.obtener_madre()}\n  Pareja: {guillermo.obtener_pareja()}\n")
    
    print(f"Objeto: Kate\n  Nombre: {kate.nombre_completo()}\n  Apellido actual: {kate.apellido()}\n  Apellido nacimiento: {kate.apellido_origen()}\n  Pareja: {kate.obtener_pareja()}\n")
