import math
class Geometria:

    def area_rectangulo(self, base, altura):
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        return (base *2)+ (altura*2) 
    
    def area_circulo(self, radio):
        return ((radio*radio)*3.141592)
    
    def perimetro_circulo(self, radio):
        return (2*math.pi)*(radio)
    
    def area_triangulo(self, base, altura):
        return (base * altura)/2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if lado1 + lado2 > lado3:
            return True
        else:
            return False
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) /2) *altura
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor)/2
    
    def area_pentagono_regular(self, lado, apotema):
        return ((lado * 5) * apotema) /2
    
    def perimetro_pentagono_regular(self, lado):
        return (lado *5)
    
    def area_hexagono_regular(self, lado, apotema):
        return((lado * 6 ) *apotema)/2
    
    def perimetro_hexagono_regular(self, lado):
        return (lado*6)
    
    def volumen_cubo(self, lado):
        return (lado*lado*lado)
    
    def area_superficie_cubo(self, lado):
        return ((lado**2)*6)
    
    
    def volumen_esfera(self, radio):
        return((4/3)*math.pi*(radio**3))
    
    def area_superficie_esfera(self, radio):
        return(4*math.pi)*(radio**2)
    
    def volumen_cilindro(self, radio, altura):
        return (math.pi*(radio**2)*(altura))
    
    def area_superficie_cilindro(self, radio, altura):
        return ((2*math.pi)*(radio**2)) + (((2*math.pi)*radio)*altura)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return (((x2-x1)**2)+(y2-y1)**2)**0.5
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2)/2),((y1+y2)/2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        return ((y2-y1)/(x2-x1))
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        return (y2 - y1, x1 - x2, x2 * y1 - x1 * y2) if x1 != x2 else (1, 0, -x1)

    def area_poligono_regular(self, num_lados, lado, apotema):
        return ((num_lados*lado)*(apotema))/2
    
    def perimetro_poligono_regular(self, num_lados, lado):
        return (num_lados * lado)
