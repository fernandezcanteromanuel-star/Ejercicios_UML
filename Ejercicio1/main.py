from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Elipse import Elipse

if __name__ == '__main__':
    # Crear objetos de cada figura geométrica
    circulo = Circulo(10, "rojo")
    cuadrado = Cuadrado(5, "azul")
    rectangulo = Rectangulo(8, 4, "verde")
    elipse = Elipse(12, 6, "amarillo")
    
    # Mostrar información de cada objeto
    print(f"Círculo - Diámetro: {circulo.get_diametro()}, Color: {circulo.get_color()}, Área: {circulo.calcular_area():.2f}")
    print(f"Cuadrado - Longitud: {cuadrado.get_longitud()}, Color: {cuadrado.get_color()}, Área: {cuadrado.calcular_area()}")
    print(f"Rectángulo - Longitud: {rectangulo.get_longitud()}, Anchura: {rectangulo.get_anchura()}, Color: {rectangulo.get_color()}, Área: {rectangulo.calcular_area()}")
    print(f"Elipse - Eje Mayor: {elipse.get_eje_mayor()}, Eje Menor: {elipse.get_eje_menor()}, Color: {elipse.get_color()}, Área: {elipse.calcular_area():.2f}")
