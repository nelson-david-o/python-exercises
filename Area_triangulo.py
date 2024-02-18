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
