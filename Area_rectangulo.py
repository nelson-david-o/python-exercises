class AreaRectangulo:

    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def formula(self):
        return self.base * self.altura

base = int(input(f'Proporcione la base: '))
altura = int(input(f'Proporcione la altura: '))
rectangulo = AreaRectangulo(base, altura)

print(f"Área del rectangulo es: {rectangulo.formula()}")


class AreaTriangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def hallarArea(self):
        return self.base * self.altura / 2

base = int(input(f'Proporcione la base del Triangulo: '))
altura = int(input(f'Proporcione la altura del Triangulo: '))

triangulo = AreaTriangulo(base,altura)
print(f'Área del triangulo es: {triangulo.hallarArea()}')

class AreaCuadrado:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def hallarAreaCuadrado(self):
        return self.lado1 * self.lado2

ResultadoArea = int(input(f'Proporcione el lado 1 del cuadrado: '))
ResultadoArea2 = int(input(f'Proporcione el lado 2 del cuadrado: '))

cuadrado = AreaCuadrado(ResultadoArea, ResultadoArea2)
print(f'Área del cuadrado es: {cuadrado.hallarAreaCuadrado()}')

class Cubo:
    def __init__(self, ancho,alto,profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundida = profundidad

    def hallarVolumen(self):
        return self.ancho * self.alto * self.profundida

v_ancho = int(input(f'Proporcione el ancho del cubo: '))
v_alto = int(input(f'Proporcione el alto del cubo: '))
v_profundidad = int(input(f'Proporcione la profundidad: '))

resultadoVolumen = Cubo(v_ancho,v_alto,v_profundidad)
print(f'Volumen de un cubo es: {resultadoVolumen.hallarVolumen()}')